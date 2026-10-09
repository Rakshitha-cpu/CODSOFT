from pathlib import Path

import pandas as pd
import streamlit as st

from recommender import JobRecommender


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Smart Job Recommendation System",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# NATIVE STREAMLIT STYLING
# No HTML strings or custom HTML cards are used.
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    h1, h2, h3 {
        letter-spacing: -0.4px;
    }

    [data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.08);
        padding: 16px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.18);
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# PATHS AND DATA LOADING
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "jobs.csv"


@st.cache_resource
def load_recommender():
    """Load the recommendation engine once."""

    return JobRecommender(data_path=DATA_PATH)


try:
    recommender = load_recommender()
    jobs_df = recommender.jobs_df.copy()

except FileNotFoundError:
    st.error(
        "The jobs.csv dataset was not found. "
        "Place jobs.csv in the same folder as app.py."
    )
    st.code(
        "Task_4_Recommendation_System/\n"
        "├── app.py\n"
        "├── recommender.py\n"
        "├── jobs.csv\n"
        "└── requirements.txt"
    )
    st.stop()

except Exception as error:
    st.error("The recommendation system could not be initialized.")
    st.exception(error)
    st.stop()


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.caption("AI-POWERED CAREER MATCHING")

st.title("💼 Smart Job Recommendation System")

st.write(
    "Discover job opportunities that align with your skills, "
    "experience, and career interests."
)

st.divider()


# ---------------------------------------------------------
# DASHBOARD METRICS
# ---------------------------------------------------------

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(
        label="Jobs Available",
        value=len(jobs_df),
    )

with metric_col2:
    company_count = jobs_df["company"].nunique()
    st.metric(
        label="Companies",
        value=company_count,
    )

with metric_col3:
    location_count = jobs_df["location"].nunique()
    st.metric(
        label="Locations",
        value=location_count,
    )


st.write("")


# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------

st.sidebar.title("🎯 Find Your Match")

st.sidebar.write(
    "Tell us what you are looking for to find relevant jobs."
)

locations = sorted(
    value
    for value in jobs_df["location"].dropna().astype(str).unique()
    if value.strip()
)

experiences = sorted(
    value
    for value in jobs_df["experience_level"].dropna().astype(str).unique()
    if value.strip()
)

location_options = ["All"] + locations
experience_options = ["All"] + experiences

selected_location = st.sidebar.selectbox(
    "Preferred Location",
    options=location_options,
    index=0,
)

selected_experience = st.sidebar.selectbox(
    "Experience Level",
    options=experience_options,
    index=0,
)

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=20,
    value=5,
)

st.sidebar.divider()

st.sidebar.caption(
    "Match scores are estimates based on skill overlap "
    "and text similarity. They are not hiring probabilities."
)


# ---------------------------------------------------------
# RECOMMENDATION TABS
# ---------------------------------------------------------

skills_tab, title_tab, browse_tab = st.tabs(
    [
        "🧠 Match by Skills",
        "💼 Match by Job Title",
        "📋 Browse Jobs",
    ]
)


# ---------------------------------------------------------
# HELPER: DISPLAY JOB CARDS
# ---------------------------------------------------------

def display_job_cards(results):
    """Display recommendation results using native Streamlit UI."""

    if results is None or results.empty:
        st.warning(
            "No matching jobs were found for these filters. "
            "Try another location or experience level."
        )
        return

    st.success(
        f"Found {len(results)} job recommendation(s)."
    )

    for rank, (_, job) in enumerate(results.iterrows(), start=1):
        title = str(job.get("job_title", "Untitled Job"))
        company = str(job.get("company", "Company Not Specified"))
        location = str(job.get("location", "Not Specified"))
        experience = str(
            job.get("experience_level", "Not Specified")
        )
        description = str(
            job.get("description", "No description available.")
        )

        try:
            score = float(job.get("match_score", 0))
        except (TypeError, ValueError):
            score = 0.0

        score = max(0.0, min(100.0, score))

        with st.container(border=True):
            title_col, score_col = st.columns([3, 1])

            with title_col:
                st.subheader(f"{rank}. {title}")
                st.write(f"🏢 **Company:** {company}")

            with score_col:
                st.metric(
                    label="Match Score",
                    value=f"{score:.2f}%",
                )

            st.progress(
                int(round(score)),
                text=f"Estimated match: {score:.2f}%",
            )

            detail_col1, detail_col2 = st.columns(2)

            with detail_col1:
                st.write(f"📍 **Location:** {location}")

            with detail_col2:
                st.write(f"🎓 **Experience:** {experience}")

            st.markdown("**Job Description**")
            st.write(
                description
                if description.strip()
                else "No description provided."
            )

            matched = str(job.get("matched_skills", "None"))
            missing = str(job.get("missing_skills", "None"))

            with st.expander("View skill analysis"):
                st.write("✅ **Matched Skills**")
                st.write(matched if matched.strip() else "None")

                st.write("📚 **Skills to Learn**")
                st.write(missing if missing.strip() else "None")

                if score < 30:
                    st.info(
                        "This job may require additional skills. "
                        "Review the missing skills before applying."
                    )
                elif score < 70:
                    st.info(
                        "You have some relevant skills. "
                        "Consider strengthening the skills listed above."
                    )
                else:
                    st.success(
                        "Your profile shows strong alignment "
                        "with this job's listed skills and text."
                    )


# ---------------------------------------------------------
# TAB 1: RECOMMEND BY SKILLS
# ---------------------------------------------------------

with skills_tab:
    st.header("Find Jobs That Match Your Skills")

    st.write(
        "Enter your technical skills, separated by commas. "
        "For example: Python, SQL, Flask, Machine Learning."
    )

    skills_input = st.text_area(
        "Your Skills",
        placeholder=(
            "Python, SQL, Flask, HTML, CSS, JavaScript"
        ),
        height=120,
        key="skills_input",
    )

    find_skills_button = st.button(
        "🔍 Find Matching Jobs",
        type="primary",
        use_container_width=True,
        key="find_skills",
    )

    if find_skills_button:
        if not skills_input.strip():
            st.warning(
                "Please enter at least one skill before searching."
            )

        else:
            try:
                with st.spinner("Analyzing your skills..."):
                    results = recommender.recommend_by_skills(
                        user_skills=skills_input,
                        top_n=top_n,
                        location_filter=selected_location,
                        experience_filter=selected_experience,
                    )

                st.session_state["skill_results"] = results
                st.session_state["skill_query"] = skills_input

            except Exception as error:
                st.error("Could not generate skill-based recommendations.")
                st.exception(error)

    if "skill_results" in st.session_state:
        st.divider()
        st.subheader("Your Skill-Based Recommendations")

        previous_query = st.session_state.get("skill_query", "")
        st.caption(f"Search query: {previous_query}")

        display_job_cards(
            st.session_state["skill_results"]
        )


# ---------------------------------------------------------
# TAB 2: RECOMMEND BY JOB TITLE
# ---------------------------------------------------------

with title_tab:
    st.header("Explore Jobs by Career Interest")

    st.write(
        "Enter the role you are interested in. "
        "The system will compare it with available job titles, "
        "skills, and descriptions."
    )

    title_input = st.text_input(
        "Desired Job Title",
        placeholder="e.g. Python Developer",
        key="title_input",
    )

    find_title_button = st.button(
        "🔍 Find Similar Jobs",
        type="primary",
        use_container_width=True,
        key="find_title",
    )

    if find_title_button:
        if not title_input.strip():
            st.warning(
                "Please enter a job title before searching."
            )

        else:
            try:
                with st.spinner("Finding relevant opportunities..."):
                    results = recommender.recommend_by_job_title(
                        job_title=title_input,
                        top_n=top_n,
                        location_filter=selected_location,
                        experience_filter=selected_experience,
                    )

                st.session_state["title_results"] = results
                st.session_state["title_query"] = title_input

            except Exception as error:
                st.error("Could not generate job-title recommendations.")
                st.exception(error)

    if "title_results" in st.session_state:
        st.divider()
        st.subheader("Your Job-Title Recommendations")

        previous_title = st.session_state.get("title_query", "")
        st.caption(f"Search query: {previous_title}")

        display_job_cards(
            st.session_state["title_results"]
        )


# ---------------------------------------------------------
# TAB 3: BROWSE ALL JOBS
# ---------------------------------------------------------

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
        placeholder="e.g. Java, Developer, TechNova",
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
            mask = mask | filtered_jobs[column].str.casefold().str.contains(
                query,
                regex=False,
                na=False,
            )

        filtered_jobs = filtered_jobs[mask]

    st.caption(
        f"{len(filtered_jobs)} job(s) match the selected filters."
    )

    if filtered_jobs.empty:
        st.info(
            "No jobs match your search. Try a different keyword "
            "or change the sidebar filters."
        )

    else:
        display_columns = [
            "job_title",
            "company",
            "location",
            "experience_level",
            "skills",
        ]

        st.dataframe(
            filtered_jobs[display_columns],
            use_container_width=True,
            hide_index=True,
        )

        csv_data = filtered_jobs.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Filtered Jobs as CSV",
            data=csv_data,
            file_name="filtered_jobs.csv",
            mime="text/csv",
            use_container_width=True,
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Smart Job Recommendation System | "
    "Built with Python, Pandas, Scikit-learn, and Streamlit"
)

st.caption(
    "Recommendations are informational and depend on the "
    "quality and completeness of the available job dataset."
            )
