
from pathlib import Path
import re

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Job Recommendation System",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# DATASET
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "jobs.csv"

REQUIRED_COLUMNS = [
    "job_id",
    "job_title",
    "company",
    "location",
    "experience_level",
    "skills",
    "description",
]

COLUMN_ALIASES = {
    "title": "job_title",
    "role": "job_title",
    "job_role": "job_title",
    "company_name": "company",
    "employer": "company",
    "city": "location",
    "experience": "experience_level",
    "required_skills": "skills",
    "job_skills": "skills",
    "job_description": "description",
}

MULTIWORD_SKILLS = [
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "data analytics",
    "natural language processing",
    "computer vision",
    "artificial intelligence",
    "spring boot",
    "android studio",
    "react native",
    "web development",
    "software development",
    "object oriented programming",
    "data structures",
    "operating systems",
    "cloud computing",
    "microsoft azure",
    "amazon web services",
    "google cloud",
    "rest api",
    "rest apis",
    "power bi",
    "node js",
    "next js",
    "user interface",
    "user experience",
    "problem solving",
    "critical thinking",
]


def normalize_text(value):
    """Normalize text for matching."""

    value = str(value or "").lower().strip()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9+#. ]+", " ", value)
    value = re.sub(r"\s+", " ", value)

    return value.strip()


def parse_skills(value):
    """Parse comma-separated or space-separated skill lists."""

    text = str(value or "").lower().strip()

    if not text:
        return []

    text = text.replace("\n", ",")
    text = text.replace(";", ",")
    text = text.replace("|", ",")

    # Preserve recognized multiword skills.
    for phrase in sorted(MULTIWORD_SKILLS, key=len, reverse=True):
        pattern = (
            r"(?<![a-z0-9])"
            + re.escape(phrase)
            + r"(?![a-z0-9])"
        )

        text = re.sub(
            pattern,
            phrase.replace(" ", "_"),
            text,
        )

    tokens = re.split(r"[, ]+", text)

    result = []

    for token in tokens:
        token = token.strip()

        if not token:
            continue

        skill = normalize_text(token.replace("_", " "))

        # Normalize common spelling variants.
        if skill == "scikit learn":
            skill = "scikit learn"

        if skill and skill not in result:
            result.append(skill)

    return result


@st.cache_data
def load_jobs(csv_path, modified_time):
    """Load and validate the job dataset."""

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Cannot find jobs.csv at {path}"
        )

    df = pd.read_csv(path)

    df.columns = [
        str(column).strip().lower().replace(" ", "_")
        for column in df.columns
    ]

    for old_name, new_name in COLUMN_ALIASES.items():
        if old_name in df.columns and new_name not in df.columns:
            df.rename(
                columns={old_name: new_name},
                inplace=True,
            )

    defaults = {
        "job_id": "",
        "job_title": "Untitled Job",
        "company": "Company Not Specified",
        "location": "Not Specified",
        "experience_level": "Not Specified",
        "skills": "",
        "description": "",
    }

    for column, default in defaults.items():
        if column not in df.columns:
            df[column] = default

    df = df[REQUIRED_COLUMNS].copy()

    for column in REQUIRED_COLUMNS:
        df[column] = (
            df[column]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    df["job_title"] = df["job_title"].replace(
        "", "Untitled Job"
    )
    df["company"] = df["company"].replace(
        "", "Company Not Specified"
    )
    df["location"] = df["location"].replace(
        "", "Not Specified"
    )
    df["experience_level"] = df["experience_level"].replace(
        "", "Not Specified"
    )

    df = df.drop_duplicates(
        subset=["job_title", "company", "location"]
    )

    if df.empty:
        raise ValueError(
            "jobs.csv does not contain any job records."
        )

    return df.reset_index(drop=True)


# =========================================================
# RECOMMENDATION ENGINE
# =========================================================

def calculate_text_similarity(query, jobs):
    """Return TF-IDF cosine similarity scores from 0 to 100."""

    if jobs.empty or not str(query).strip():
        return [0.0] * len(jobs)

    documents = (
        jobs["job_title"].fillna("")
        + " "
        + jobs["skills"].fillna("")
        + " "
        + jobs["description"].fillna("")
    ).tolist()

    try:
        vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
            token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9+#.]*\b",
        )

        matrix = vectorizer.fit_transform(
            documents + [str(query)]
        )

        similarities = cosine_similarity(
            matrix[-1],
            matrix[:-1],
        ).flatten()

        return (similarities * 100).tolist()

    except ValueError:
        return [0.0] * len(jobs)


def recommend_jobs(
    jobs,
    mode,
    query,
    top_n,
    location_filter,
    experience_filter,
):
    """Generate skill-based or job-title-based recommendations."""

    df = jobs.copy()

    if location_filter != "All":
        df = df[
            df["location"].str.casefold()
            == location_filter.casefold()
        ]

    if experience_filter != "All":
        df = df[
            df["experience_level"].str.casefold()
            == experience_filter.casefold()
        ]

    df = df.reset_index(drop=True)

    if df.empty:
        return df

    user_skills = (
        parse_skills(query)
        if mode == "skills"
        else []
    )

    similarities = calculate_text_similarity(query, df)

    match_scores = []
    skill_scores = []
    matched_results = []
    missing_results = []

    for index, (_, job) in enumerate(df.iterrows()):

        required_skills = parse_skills(job["skills"])

        user_set = set(user_skills)
        required_set = set(required_skills)

        matched = sorted(user_set.intersection(required_set))
        missing = sorted(required_set.difference(user_set))

        if required_set:
            skill_score = (
                len(matched) / len(required_set)
            ) * 100
        else:
            skill_score = 0.0

        similarity_score = similarities[index]

        if mode == "skills":
            # Skill matching is the primary factor.
            final_score = (
                0.80 * skill_score
                + 0.20 * similarity_score
            )
        else:
            # Job-title mode ranks by textual relevance.
            final_score = similarity_score

        skill_scores.append(round(skill_score, 2))
        match_scores.append(round(final_score, 2))

        matched_results.append(
            ", ".join(matched) if matched else "None"
        )
        missing_results.append(
            ", ".join(missing) if missing else "None"
        )

    df["skill_score"] = skill_scores
    df["similarity_score"] = [
        round(value, 2) for value in similarities
    ]
    df["match_score"] = match_scores
    df["matched_skills"] = matched_results
    df["missing_skills"] = missing_results

    df = df.sort_values(
        by=["match_score", "skill_score"],
        ascending=False,
    )

    return df.head(top_n).reset_index(drop=True)


# =========================================================
# LOAD DATA
# =========================================================

try:
    if not DATA_PATH.exists():
        st.error(
            "jobs.csv was not found. "
            "Upload it to the same folder as app.py."
        )
        st.code(
            "Task_4_Recommendation_System/\n"
            "├── app.py\n"
            "├── recommender.py\n"
            "├── jobs.csv\n"
            "└── requirements.txt"
        )
        st.stop()

    jobs_df = load_jobs(
        str(DATA_PATH),
        DATA_PATH.stat().st_mtime,
    )

except Exception as error:
    st.error("Could not load the job dataset.")
    st.exception(error)
    st.stop()


# =========================================================
# DASHBOARD HEADER
# =========================================================

st.caption("AI-POWERED CAREER MATCHING")

st.title("💼 Smart Job Recommendation System")

st.write(
    "Discover career opportunities that align with your skills, "
    "experience, and professional interests."
)

st.divider()


# =========================================================
# METRICS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Available Jobs", len(jobs_df))

with col2:
    st.metric("Companies", jobs_df["company"].nunique())

with col3:
    st.metric("Locations", jobs_df["location"].nunique())

st.write("")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎯 Job Preferences")

locations = sorted(
    value
    for value in jobs_df["location"].unique()
    if value.strip()
)

experiences = sorted(
    value
    for value in jobs_df["experience_level"].unique()
    if value.strip()
)

selected_location = st.sidebar.selectbox(
    "Preferred Location",
    ["All"] + locations,
)

selected_experience = st.sidebar.selectbox(
    "Experience Level",
    ["All"] + experiences,
)

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=20,
    value=5,
)

st.sidebar.divider()

st.sidebar.caption(
    "Match scores estimate relevance using the available job data. "
    "They are not probabilities of getting hired."
)


# =========================================================
# DISPLAY RECOMMENDATIONS
# =========================================================

def display_job_cards(results):

    if results is None or results.empty:
        st.warning(
            "No jobs matched these filters. "
            "Try another query or change the filters."
        )
        return

    st.success(
        f"Found {len(results)} relevant job(s)."
    )

    for rank, (_, job) in enumerate(
        results.iterrows(),
        start=1,
    ):

        score = max(
            0.0,
            min(100.0, float(job["match_score"])),
        )

        with st.container(border=True):

            title_col, score_col = st.columns([3, 1])

            with title_col:
                st.subheader(
                    f"{rank}. {job['job_title']}"
                )
                st.write(
                    f"🏢 **Company:** {job['company']}"
                )

            with score_col:
                st.metric(
                    "Match Score",
                    f"{score:.2f}%",
                )

            st.progress(
                int(round(score)),
                text=f"Estimated match: {score:.2f}%",
            )

            info_col1, info_col2 = st.columns(2)

            with info_col1:
                st.write(
                    f"📍 **Location:** {job['location']}"
                )

            with info_col2:
                st.write(
                    f"🎓 **Experience:** "
                    f"{job['experience_level']}"
                )

            st.markdown("**Job Description**")

            st.write(
                job["description"]
                if job["description"].strip()
                else "No description provided."
            )

            with st.expander("View Skill Analysis"):

                st.write("✅ **Matched Skills**")
                st.write(job["matched_skills"])

                st.write("📚 **Skills to Learn**")
                st.write(job["missing_skills"])

                if score >= 70:
                    st.success(
                        "Strong alignment with the available job information."
                    )
                elif score >= 30:
                    st.info(
                        "Some alignment found. Review the missing skills."
                    )
                else:
                    st.info(
                        "Consider developing additional relevant skills."
                    )


# =========================================================
# TABS
# =========================================================

skills_tab, title_tab, browse_tab = st.tabs(
    [
        "🧠 Match by Skills",
        "💼 Match by Job Title",
        "📋 Browse Jobs",
    ]
)


# =========================================================
# SKILL SEARCH
# =========================================================

with skills_tab:

    st.header("Find Jobs That Match Your Skills")

    st.write(
        "Enter your skills separated by commas. "
        "Example: Python, SQL, Flask, Machine Learning."
    )

    skills_input = st.text_area(
        "Your Skills",
        placeholder="Python, SQL, Flask, HTML, CSS, JavaScript",
        height=110,
        key="skills_input",
    )

    if st.button(
        "🔍 Find Matching Jobs",
        type="primary",
        use_container_width=True,
        key="skills_button",
    ):

        if not skills_input.strip():
            st.warning("Enter at least one skill.")

        else:
            results = recommend_jobs(
                jobs=jobs_df,
                mode="skills",
                query=skills_input,
                top_n=top_n,
                location_filter=selected_location,
                experience_filter=selected_experience,
            )

            st.session_state["skill_results"] = results
            st.session_state["skill_query"] = skills_input

    if "skill_results" in st.session_state:

        st.divider()
        st.subheader("Your Recommendations")

        st.caption(
            "Skills entered: "
            + st.session_state.get("skill_query", "")
        )

        display_job_cards(
            st.session_state["skill_results"]
        )


# =========================================================
# JOB TITLE SEARCH
# =========================================================

with title_tab:

    st.header("Explore Jobs by Career Interest")

    st.write(
        "Enter a job title to find relevant opportunities "
        "based on job titles, required skills, and descriptions."
    )

    title_input = st.text_input(
        "Desired Job Title",
        placeholder="e.g. Python Developer",
        key="title_input",
    )

    if st.button(
        "🔍 Find Similar Jobs",
        type="primary",
        use_container_width=True,
        key="title_button",
    ):

        if not title_input.strip():
            st.warning("Enter a job title.")

        else:
            results = recommend_jobs(
                jobs=jobs_df,
                mode="title",
                query=title_input,
                top_n=top_n,
                location_filter=selected_location,
                experience_filter=selected_experience,
            )

            st.session_state["title_results"] = results
            st.session_state["title_query"] = title_input

    if "title_results" in st.session_state:

        st.divider()
        st.subheader("Recommended Jobs")

        st.caption(
            "Career interest: "
            + st.session_state.get("title_query", "")
        )

        display_job_cards(
            st.session_state["title_results"]
        )


# =========================================================
# BROWSE JOBS
# =========================================================

with browse_tab:

    st.header("Browse Available Opportunities")

    filtered_jobs = jobs_df.copy()

    if selected_location != "All":
        filtered_jobs = filtered_jobs[
            filtered_jobs["location"].str.casefold()
            == selected_location.casefold()
        ]

    if selected_experience != "All":
        filtered_jobs = filtered_jobs[
            filtered_jobs["experience_level"].str.casefold()
            == selected_experience.casefold()
        ]

    search_text = st.text_input(
        "Search jobs or companies",
        placeholder="e.g. Python, Developer, TechNova",
        key="browse_search",
    )

    if search_text.strip():

        query = search_text.strip().casefold()

        searchable_columns = [
            "job_title",
            "company",
            "location",
            "experience_level",
            "skills",
            "description",
        ]

        mask = pd.Series(
            False,
            index=filtered_jobs.index,
        )

        for column in searchable_columns:
            mask |= filtered_jobs[column].str.casefold().str.contains(
                query,
                regex=False,
                na=False,
            )

        filtered_jobs = filtered_jobs[mask]

    st.caption(
        f"{len(filtered_jobs)} job(s) match your filters."
    )

    if filtered_jobs.empty:
        st.info("No jobs matched your search.")

    else:

        st.dataframe(
            filtered_jobs[
                [
                    "job_title",
                    "company",
                    "location",
                    "experience_level",
                    "skills",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

        st.download_button(
            "⬇️ Download Filtered Jobs as CSV",
            data=filtered_jobs.to_csv(index=False).encode("utf-8"),
            file_name="filtered_jobs.csv",
            mime="text/csv",
            use_container_width=True,
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Smart Job Recommendation System | "
    "Python · Pandas · Scikit-learn · Streamlit"
)

st.caption(
    "Recommendations depend on the completeness of the job dataset."
)
