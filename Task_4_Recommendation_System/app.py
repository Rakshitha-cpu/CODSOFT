
from pathlib import Path

import pandas as pd
import streamlit as st

from recommender import JobRecommender


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
# DATASET PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "jobs.csv"


# =========================================================
# LOAD RECOMMENDATION ENGINE
# =========================================================

@st.cache_resource
def load_recommender():
    """Create the recommendation engine."""

    return JobRecommender(data_path=DATA_PATH)


try:
    recommender = load_recommender()

    # Both attributes are provided by the matching recommender.py.
    jobs_df = recommender.jobs_df.copy()

except Exception as error:
    st.error("The recommendation system could not be initialized.")

    st.write(
        "Check that app.py, recommender.py, and jobs.csv "
        "are present in the same folder."
    )

    st.exception(error)
    st.stop()


# =========================================================
# HEADER
# =========================================================

st.caption("AI-POWERED CAREER MATCHING")

st.title("💼 Smart Job Recommendation System")

st.write(
    "Discover job opportunities that align with your skills, "
    "experience, and career interests."
)

st.divider()


# =========================================================
# DASHBOARD METRICS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Available Jobs",
        value=len(jobs_df),
    )

with col2:
    st.metric(
        label="Companies",
        value=jobs_df["company"].nunique(),
    )

with col3:
    st.metric(
        label="Locations",
        value=jobs_df["location"].nunique(),
    )


st.write("")


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.title("🎯 Job Preferences")

st.sidebar.write(
    "Customize your search to discover relevant opportunities."
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
    "Match scores are estimates based on listed skills and text similarity. "
    "They do not represent the probability of receiving a job offer."
)


# =========================================================
# JOB CARD DISPLAY
# =========================================================

def display_job_cards(results):
    """Display recommendations using native Streamlit components."""

    if results is None or results.empty:
        st.warning(
            "No matching jobs were found. Try changing your filters "
            "or entering different skills."
        )
        return

    st.success(f"Found {len(results)} recommendation(s).")

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

        # Ensure progress values remain within 0–100.
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

            info_col1, info_col2 = st.columns(2)

            with info_col1:
                st.write(f"📍 **Location:** {location}")

            with info_col2:
                st.write(f"🎓 **Experience:** {experience}")

            st.markdown("**Job Description**")

            st.write(
                description
                if description.strip()
                else "No description provided."
            )

            with st.expander("View Skill Analysis"):

                matched = str(job.get("matched_skills", "None"))
                missing = str(job.get("missing_skills", "None"))

                st.write("✅ **Matched Skills**")
                st.write(matched if matched.strip() else "None")

                st.write("📚 **Skills to Learn**")
                st.write(missing if missing.strip() else "None")

                if score >= 70:
                    st.success(
                        "Strong alignment with the listed job requirements."
                    )
                elif score >= 30:
                    st.info(
                        "Some alignment found. Review the missing skills "
                        "to identify areas for improvement."
                    )
                else:
                    st.info(
                        "This role may require additional skills or a "
                        "different background."
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
# TAB 1: SKILL-BASED RECOMMENDATIONS
# =========================================================

with skills_tab:

    st.header("Find Jobs That Match Your Skills")

    st.write(
        "Enter your technical skills, separated by commas. "
        "For example: Python, SQL, Flask, Machine Learning."
    )

    skills_input = st.text_area(
        "Your Skills",
        placeholder="Python, SQL, Flask, HTML, CSS, JavaScript",
        height=120,
        key="skills_input",
    )

    if st.button(
        "🔍 Find Matching Jobs",
        type="primary",
        use_container_width=True,
        key="find_skills",
    ):

        if not skills_input.strip():
            st.warning("Please enter at least one skill.")

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
        st.subheader("Your Recommendations")

        st.caption(
            "Skills entered: "
            + st.session_state.get("skill_query", "")
        )

        display_job_cards(
            st.session_state["skill_results"]
        )


# =========================================================
# TAB 2: JOB-TITLE RECOMMENDATIONS
# =========================================================

with title_tab:

    st.header("Explore Jobs by Career Interest")

    st.write(
        "Enter a role you are interested in. The system compares "
        "your query with available job titles, skills, and descriptions."
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
        key="find_title",
    ):

        if not title_input.strip():
            st.warning("Please enter a job title.")

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
        st.subheader("Recommended Jobs")

        st.caption(
            "Career interest: "
            + st.session_state.get("title_query", "")
        )

        display_job_cards(
            st.session_state["title_results"]
        )


# =========================================================
# TAB 3: BROWSE AND DOWNLOAD JOBS
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
        f"{len(filtered_jobs)} job(s) match your current filters."
    )

    if filtered_jobs.empty:

        st.info(
            "No jobs match your search. Try a different keyword "
            "or adjust the sidebar filters."
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
            label="⬇️ Download Jobs as CSV",
            data=csv_data,
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
    "Recommendations depend on the available dataset and should "
    "be used as guidance when exploring career opportunities."
            )
