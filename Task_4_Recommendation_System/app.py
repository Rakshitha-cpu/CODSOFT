import html
from pathlib import Path

import streamlit as st
import pandas as pd

from recommender import JobRecommender


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Job Recommendation System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    .hero {
        padding: 35px;
        border-radius: 24px;
        background: linear-gradient(120deg, #312e81, #4f46e5, #7c3aed);
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 12px 30px rgba(79, 70, 229, 0.18);
    }

    .hero-label {
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 12px;
        font-weight: 700;
        color: #ddd6fe;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 36px;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        font-size: 16px;
        line-height: 1.7;
        color: #ede9fe;
        max-width: 750px;
    }

    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 9px;
        margin-top: 22px;
    }

    .badge {
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.25);
        padding: 8px 13px;
        border-radius: 20px;
        font-size: 12px;
        color: white;
    }

    .feature-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 17px;
        padding: 20px;
        min-height: 155px;
        box-shadow: 0 5px 18px rgba(31,41,55,0.04);
    }

    .feature-icon {
        font-size: 27px;
        margin-bottom: 8px;
    }

    .feature-title {
        color: #312e81;
        font-size: 16px;
        font-weight: 750;
        margin-bottom: 7px;
    }

    .feature-text {
        color: #64748b;
        font-size: 13px;
        line-height: 1.6;
    }

    .section-heading {
        color: #1e1b4b;
        font-size: 24px;
        font-weight: 800;
        margin-top: 28px;
        margin-bottom: 15px;
    }

    .job-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 24px;
        margin: 12px 0;
        box-shadow: 0 6px 20px rgba(31,41,55,0.05);
    }

    .job-top {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        align-items: flex-start;
    }

    .job-rank {
        display: inline-block;
        background: #ede9fe;
        color: #5b21b6;
        border-radius: 9px;
        padding: 5px 10px;
        font-size: 12px;
        font-weight: 800;
        margin-bottom: 9px;
    }

    .job-title {
        font-size: 22px;
        font-weight: 800;
        color: #1e1b4b;
        margin-bottom: 6px;
    }

    .job-meta {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 15px;
    }

    .score-number {
        color: #4f46e5;
        font-size: 25px;
        font-weight: 850;
        text-align: right;
        white-space: nowrap;
    }

    .score-label {
        color: #64748b;
        font-size: 11px;
        text-align: right;
    }

    .score-track {
        height: 9px;
        border-radius: 20px;
        background: #e9eaf5;
        overflow: hidden;
        margin: 10px 0 18px;
    }

    .score-fill {
        height: 100%;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        border-radius: 20px;
    }

    .job-desc {
        color: #475569;
        font-size: 14px;
        line-height: 1.7;
        margin-bottom: 16px;
    }

    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 18px;
    }

    .pill {
        background: #f1f5f9;
        color: #475569;
        border-radius: 20px;
        padding: 7px 11px;
        font-size: 12px;
    }

    .skill-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
    }

    .skill-box {
        padding: 13px;
        border-radius: 12px;
        font-size: 12px;
        line-height: 1.8;
        overflow-wrap: anywhere;
    }

    .skill-box b {
        display: block;
        margin-bottom: 5px;
        font-size: 12px;
    }

    .required {
        background: #f1f5f9;
        color: #334155;
    }

    .matched {
        background: #dcfce7;
        color: #166534;
    }

    .missing {
        background: #ffedd5;
        color: #9a3412;
    }

    .metric-card {
        background: white;
        border: 1px solid #e5e7eb;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(31,41,55,0.04);
    }

    .metric-label {
        color: #64748b;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #312e81;
        font-size: 29px;
        font-weight: 850;
        margin-top: 8px;
    }

    .info-panel {
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        border-radius: 16px;
        padding: 20px;
        color: #312e81;
        line-height: 1.8;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding: 30px 0 10px;
        font-size: 12px;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 23px;
        }

        .hero-title {
            font-size: 27px;
        }

        .skill-grid {
            grid-template-columns: 1fr;
        }

        .job-title {
            font-size: 19px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def safe_text(value, default="Not specified"):
    """Convert a value to safe display text."""
    if value is None:
        return default

    try:
        if pd.isna(value):
            return default
    except (TypeError, ValueError):
        pass

    value = str(value).strip()

    if not value:
        return default

    return html.escape(value)


def format_score(value):
    """Format a recommendation score as a percentage."""
    try:
        score = float(value)
    except (TypeError, ValueError):
        score = 0.0

    return max(0.0, min(100.0, score))


def display_skills(value):
    """Display a skill list without exposing Python list syntax."""
    if value is None:
        return "None"

    try:
        if pd.isna(value):
            return "None"
    except (TypeError, ValueError):
        pass

    if isinstance(value, (list, tuple, set)):
        items = [str(item).strip() for item in value if str(item).strip()]
        return html.escape(", ".join(items)) if items else "None"

    text = str(value).strip()

    if not text or text.lower() in {"none", "nan", "[]"}:
        return "None"

    # Support comma-separated or list-like skill output.
    text = text.strip("[]")
    items = [
        item.strip().strip("'\"")
        for item in text.replace(";", ",").split(",")
        if item.strip().strip("'\"")
    ]

    if not items:
        return "None"

    return html.escape(", ".join(items))


def get_column_value(row, column, default="Not specified"):
    """Read a DataFrame field safely."""
    if column not in row.index:
        return default
    return row[column]


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-label">AI-Powered Career Matching</div>
        <div class="hero-title">Smart Job Recommendation System</div>
        <div class="hero-subtitle">
            Discover suitable job opportunities using your skills,
            preferred location, experience level, and intelligent
            content-based recommendations.
        </div>
        <div class="badge-row">
            <span class="badge">Content-Based Filtering</span>
            <span class="badge">TF-IDF Vectorization</span>
            <span class="badge">Cosine Similarity</span>
            <span class="badge">Skill Gap Analysis</span>
            <span class="badge">Match Scoring</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------

feature_columns = st.columns(3)

features = [
    (
        "🎯",
        "Personalized Matching",
        "Find jobs based on candidate skills, preferred role, experience level, and location.",
    ),
    (
        "📊",
        "Match Score",
        "Compare your skills and profile with job requirements to estimate compatibility.",
    ),
    (
        "🧠",
        "Skill Gap Analysis",
        "Identify matching and missing skills to plan your next learning steps.",
    ),
]

for column, feature in zip(feature_columns, features):
    icon, title, description = feature

    with column:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-text">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# --------------------------------------------------
# LOAD RECOMMENDER
# --------------------------------------------------

@st.cache_resource
def load_recommender():
    # Resolve the dataset relative to this app's folder.
    data_path = Path(__file__).resolve().parent / "jobs.csv"

    if not data_path.exists():
        raise FileNotFoundError(
            f"Could not find jobs.csv at: {data_path}. "
            "Make sure jobs.csv is committed inside Task_4_Recommendation_System."
        )

    # Support recommender implementations that accept a path
    # and those that load their dataset using a default path.
    try:
        return JobRecommender(data_path=str(data_path))
    except TypeError:
        return JobRecommender()


try:
    recommender = load_recommender()
except Exception as exc:
    st.error("The recommendation engine could not be loaded.")
    st.exception(exc)
    st.stop()


# --------------------------------------------------
# CANDIDATE PREFERENCES
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">Candidate Preferences</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1])

with left:
    mode = st.radio(
        "Recommendation Mode",
        ["Recommend by Skills", "Recommend by Job Role"],
        horizontal=True,
    )

    top_n = st.select_slider(
        "Number of recommendations",
        options=[3, 5, 8, 10],
        value=5,
    )

with right:
    jobs_df = getattr(recommender, "jobs", pd.DataFrame())

    if not isinstance(jobs_df, pd.DataFrame):
        jobs_df = pd.DataFrame()

    if not jobs_df.empty and "location" in jobs_df.columns:
        locations = sorted(
            jobs_df["location"].dropna().astype(str).unique().tolist()
        )
    else:
        locations = []

    location_options = ["All"] + locations

    location_filter = st.selectbox(
        "Preferred Location",
        location_options,
        index=0,
    )

    if not jobs_df.empty and "experience_level" in jobs_df.columns:
        experiences = sorted(
            jobs_df["experience_level"].dropna().astype(str).unique().tolist()
        )
    else:
        experiences = []

    experience_options = ["All"] + experiences

    experience_filter = st.selectbox(
        "Experience Level",
        experience_options,
        index=0,
    )


user_skills = ""
selected_job = None

if mode == "Recommend by Skills":
    user_skills = st.text_input(
        "Enter your skills",
        placeholder="Example: Python, SQL, Flask, HTML, CSS, Java",
        help="Separate skills using commas.",
    )

    st.caption(
        "Tip: Enter the technologies you know, separated by commas, "
        "to receive more relevant recommendations."
    )

else:
    if not jobs_df.empty and "job_title" in jobs_df.columns:
        job_titles = sorted(
            jobs_df["job_title"].dropna().astype(str).unique().tolist()
        )

        if job_titles:
            selected_job = st.selectbox(
                "Select a job role you like",
                job_titles,
            )

            if selected_job:
                selected_rows = jobs_df[
                    jobs_df["job_title"].astype(str) == selected_job
                ]

                if not selected_rows.empty:
                    selected = selected_rows.iloc[0]

                    st.markdown(
                        f"""
                        <div class="info-panel">
                            <b>Selected Role:</b>
                            {safe_text(selected_job)}<br>
                            <b>Company:</b>
                            {safe_text(get_column_value(selected, "company"))}<br>
                            <b>Location:</b>
                            {safe_text(get_column_value(selected, "location"))}<br>
                            <b>Experience:</b>
                            {safe_text(get_column_value(selected, "experience_level"))}<br>
                            <b>Required Skills:</b>
                            {display_skills(get_column_value(selected, "skills", ""))}<br>
                            <b>Description:</b>
                            {safe_text(get_column_value(selected, "description"))}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
    else:
        st.warning(
            "The dataset does not contain job titles. "
            "Check that jobs.csv has a job_title column."
        )


# --------------------------------------------------
# HOW THE ENGINE WORKS
# --------------------------------------------------

with st.expander("⚙️ How the engine works"):
    st.markdown(
        """
        1. **Job data:** The engine reads job titles, skills,
           experience levels, locations, and descriptions.
        2. **TF-IDF vectorization:** Text is transformed into numerical
           vectors based on term importance.
        3. **Cosine similarity:** Textual similarity is used to compare
           job descriptions and candidate/job-role information.
        4. **Skill-gap analysis:** The system identifies overlapping
           skills and skills that may need improvement.
        5. **Filtering:** Location and experience preferences narrow
           the list of recommendations.
        """
    )


# --------------------------------------------------
# GENERATE RECOMMENDATIONS
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">Recommended Jobs</div>',
    unsafe_allow_html=True,
)

recommend_clicked = st.button(
    "✨ Find Matching Jobs",
    type="primary",
    use_container_width=True,
)

if recommend_clicked:
    try:
        if mode == "Recommend by Skills":
            if not user_skills.strip():
                st.warning("Please enter at least one skill to continue.")
                st.stop()

            results = recommender.recommend_by_skills(
                user_skills,
                top_n,
                location_filter,
                experience_filter,
            )

        else:
            if not selected_job:
                st.warning("Please select a job role.")
                st.stop()

            results = recommender.recommend_by_job_title(
                selected_job,
                top_n,
                location_filter,
                experience_filter,
            )

        if results is None or not isinstance(results, pd.DataFrame):
            st.error(
                "The recommender did not return a pandas DataFrame. "
                "Check the return value in recommender.py."
            )
            st.stop()

        if results.empty:
            st.warning(
                "No jobs matched these filters. Try choosing All for "
                "location or experience, or select a different role."
            )
            st.stop()

        # Make sure scores are numeric before displaying metrics.
        if "match_score" not in results.columns:
            st.error(
                "The recommendation results do not contain a "
                "'match_score' column. Update recommender.py to "
                "return match_score for each job."
            )
            st.stop()

        results = results.copy()
        results["match_score"] = pd.to_numeric(
            results["match_score"],
            errors="coerce",
        ).fillna(0).clip(0, 100)

        scores = results["match_score"]

        metric_columns = st.columns(3)

        metrics = [
            ("RESULTS", str(len(results))),
            ("AVG MATCH", f"{scores.mean():.2f}%"),
            ("BEST MATCH", f"{scores.max():.2f}%"),
        ]

        for column, metric in zip(metric_columns, metrics):
            label, value = metric

            with column:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">{value}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.write("")

        # Render each job as a complete HTML card.
        for index, (_, row) in enumerate(results.iterrows(), start=1):
            job_title = safe_text(get_column_value(row, "job_title"))
            company = safe_text(get_column_value(row, "company"))
            location = safe_text(get_column_value(row, "location"))
            experience = safe_text(
                get_column_value(row, "experience_level")
            )
            description = safe_text(
                get_column_value(row, "description", "No description available.")
            )

            required_skills = display_skills(
                get_column_value(row, "skills", "")
            )
            matched_skills = display_skills(
                get_column_value(row, "matched_skills", None)
            )
            missing_skills = display_skills(
                get_column_value(row, "missing_skills", None)
            )

            score = format_score(row["match_score"])

            st.markdown(
                f"""
                <div class="job-card">
                    <div class="job-top">
                        <div>
                            <div class="job-rank">#{index}</div>
                            <div class="job-title">{job_title}</div>
                            <div class="job-meta">
                                {company} · {location}
                            </div>
                        </div>
                        <div>
                            <div class="score-number">{score:.2f}%</div>
                            <div class="score-label">MATCH SCORE</div>
                        </div>
                    </div>

                    <div class="score-track">
                        <div class="score-fill"
                             style="width: {score:.2f}%;">
                        </div>
                    </div>

                    <div class="job-desc">{description}</div>

                    <div class="pill-row">
                        <span class="pill">📍 {location}</sp
