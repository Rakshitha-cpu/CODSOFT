from pathlib import Path
import html

import pandas as pd
import streamlit as st

from recommender import JobRecommender


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Smart Job Recommendation System",
    page_icon="🎯",
    layout="wide",
)


# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7ff, #eef2ff);
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        background: linear-gradient(120deg, #312e81, #4f46e5, #7c3aed);
        color: white;
        padding: 35px;
        border-radius: 22px;
        margin-bottom: 25px;
    }

    .hero-label {
        color: #ddd6fe;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 35px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        font-size: 15px;
        line-height: 1.8;
        color: #ede9fe;
    }

    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 20px;
    }

    .badge {
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.3);
        padding: 8px 12px;
        border-radius: 20px;
        font-size: 12px;
    }

    .feature-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 20px;
        min-height: 145px;
        margin-bottom: 15px;
    }

    .feature-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .feature-title {
        color: #312e81;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 8px;
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
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .info-panel {
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        border-radius: 14px;
        padding: 18px;
        color: #312e81;
        line-height: 1.8;
        margin: 12px 0;
    }

    .metric-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }

    .metric-label {
        color: #64748b;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #4f46e5;
        font-size: 28px;
        font-weight: 800;
        margin-top: 8px;
    }

    .job-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: 0 5px 18px rgba(31,41,55,0.05);
    }

    .job-rank {
        display: inline-block;
        background: #ede9fe;
        color: #5b21b6;
        padding: 5px 10px;
        border-radius: 8px;
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 8px;
    }

    .job-title {
        color: #1e1b4b;
        font-size: 22px;
        font-weight: 800;
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
        font-weight: 800;
        text-align: right;
    }

    .score-label {
        color: #64748b;
        font-size: 11px;
        text-align: right;
    }

    .score-track {
        background: #e9eaf5;
        height: 9px;
        border-radius: 20px;
        overflow: hidden;
        margin: 12px 0 18px;
    }

    .score-fill {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        height: 9px;
        border-radius: 20px;
    }

    .job-desc {
        color: #475569;
        font-size: 14px;
        line-height: 1.7;
        margin-bottom: 15px;
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
        padding: 7px 11px;
        border-radius: 20px;
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

    .footer {
        color: #64748b;
        text-align: center;
        padding: 30px 0 10px;
        font-size: 12px;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 22px;
        }

        .hero-title {
            font-size: 27px;
        }

        .skill-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# HELPER FUNCTIONS
# ==================================================

def safe_text(value, default="Not specified"):
    """Escape values before displaying them in HTML."""

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
    """Convert a score into a percentage between 0 and 100."""

    try:
        score = float(value)
    except (TypeError, ValueError):
        score = 0.0

    return max(0.0, min(100.0, score))


def display_skills(value):
    """Format skills for display."""

    if value is None:
        return "None"

    try:
        if pd.isna(value):
            return "None"
    except (TypeError, ValueError):
        pass

    if isinstance(value, (list, tuple, set)):
        items = [str(item).strip() for item in value if str(item).strip()]
    else:
        text = str(value).strip()

        if text.lower() in {"", "none", "nan", "[]"}:
            return "None"

        text = text.strip("[]")
        items = [
            item.strip().strip("'\"")
            for item in text.replace(";", ",").split(",")
            if item.strip().strip("'\"")
        ]

    if not items:
        return "None"

    return html.escape(", ".join(items))


def get_value(row, column, default="Not specified"):
    """Read a field from a result row."""

    if column not in row.index:
        return default

    return row[column]


# ==================================================
# HERO SECTION
# ==================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-label">AI-Powered Career Matching</div>

        <div class="hero-title">
            Smart Job Recommendation System
        </div>

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


# ==================================================
# FEATURE CARDS
# ==================================================

columns = st.columns(3)

features = [
    (
        "🎯",
        "Personalized Matching",
        "Find jobs based on your skills, preferred role, experience, and location.",
    ),
    (
        "📊",
        "Match Score",
        "Estimate compatibility using overlapping skills and job information.",
    ),
    (
        "🧠",
        "Skill Gap Analysis",
        "Identify matching and missing skills to plan your learning journey.",
    ),
]

for column, feature in zip(columns, features):
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


# ==================================================
# LOAD DATA AND RECOMMENDER
# ==================================================

@st.cache_resource
def load_recommender():
    data_path = Path(__file__).resolve().parent / "jobs.csv"

    if not data_path.exists():
        raise FileNotFoundError(
            "jobs.csv is missing. Place it in the same folder as app.py."
        )

    try:
        return JobRecommender(data_path=str(data_path))
    except TypeError:
        return JobRecommender()


try:
    recommender = load_recommender()
except Exception as error:
    st.error("Unable to load the recommendation engine.")
    st.exception(error)
    st.stop()


jobs_df = getattr(recommender, "jobs", pd.DataFrame())

if not isinstance(jobs_df, pd.DataFrame):
    jobs_df = pd.DataFrame()


# ==================================================
# CANDIDATE PREFERENCES
# ==================================================

st.markdown(
    '<div class="section-heading">Candidate Preferences</div>',
    unsafe_allow_html=True,
)

left_column, right_column = st.columns(2)

with left_column:
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

with right_column:
    if "location" in jobs_df.columns:
        locations = sorted(
            jobs_df["location"].dropna().astype(str).unique().tolist()
        )
    else:
        locations = []

    location_filter = st.selectbox(
        "Preferred Location",
        ["All"] + locations,
    )

    if "experience_level" in jobs_df.columns:
        experiences = sorted(
            jobs_df["experience_level"].dropna().astype(str).unique().tolist()
        )
    else:
        experiences = []

    experience_filter = st.selectbox(
        "Experience Level",
        ["All"] + experiences,
    )


user_skills = ""
selected_job = None

if mode == "Recommend by Skills":
    user_skills = st.text_input(
        "Enter your skills",
        placeholder="Python, SQL, Flask, HTML, CSS, Java",
        help="Enter your skills separated by commas.",
    )

else:
    if "job_title" not in jobs_df.columns or jobs_df.empty:
        st.warning("No job titles found. Check your jobs.csv file.")
    else:
        job_titles = sorted(
            jobs_df["job_title"].dropna().astype(str).unique().tolist()
        )

        if job_titles:
            selected_job = st.selectbox(
                "Select a job role you like",
                job_titles,
            )

            matching_rows = jobs_df[
                jobs_df["job_title"].astype(str) == selected_job
            ]

            if not matching_rows.empty:
                selected_row = matching_rows.iloc[0]

                st.markdown(
                    f"""
                    <div class="info-panel">
                        <b>Selected Role:</b> {safe_text(selected_job)}<br>
                        <b>Company:</b> {safe_text(get_value(selected_row, "company"))}<br>
                        <b>Location:</b> {safe_text(get_value(selected_row, "location"))}<br>
                        <b>Experience:</b> {safe_text(get_value(selected_row, "experience_level"))}<br>
                        <b>Required Skills:</b> {display_skills(get_value(selected_row, "skills", ""))}<br>
                        <b>Description:</b> {safe_text(get_value(selected_row, "description"))}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


# ==================================================
# EXPLANATION
# ==================================================

with st.expander("⚙️ How the engine works"):
    st.markdown(
        """
        **1. Job information:** The system uses job titles, required
        skills, experience levels, locations, and descriptions.

        **2. TF-IDF vectorization:** Text is converted into numerical
        vectors based on the importance of terms.

        **3. Cosine similarity:** The engine compares textual
        representations to estimate similarity.

        **4. Skill-gap analysis:** Matching and missing skills are
        displayed for each recommendation.

        **5. Filtering:** Location and experience preferences narrow
        the results.
        """
    )


# ==================================================
# RECOMMENDATION RESULTS
# ==================================================

st.markdown(
    '<div class="section-heading">Recommended Jobs</div>',
    unsafe_allow_html=True,
)

if st.button(
    "✨ Find Matching Jobs",
    type="primary",
    use_container_width=True,
):
    try:
        if mode == "Recommend by Skills":
            if not user_skills.strip():
                st.warning("Please enter your skills first.")
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

        if not isinstance(results, pd.DataFrame):
            st.error("The recommender must return a pandas DataFrame.")
            st.stop()

        if results.empty:
            st.warning(
                "No matching jobs found. Try changing the location "
                "or experience filters."
            )
            st.stop()

        if "match_score" not in results.columns:
            st.error(
                "Missing match_score column. Please check recommender.py."
            )
            st.stop()

        results = results.copy()

        results["match_score"] = pd.to_numeric(
            results["match_score"],
            errors="coerce",
        ).fillna(0).clip(0, 100)

        scores = results["match_score"]

        metrics = st.columns(3)

        metric_data = [
            ("RESULTS", str(len(results))),
            ("AVG MATCH", f"{scores.mean():.2f}%"),
            ("BEST MATCH", f"{scores.max():.2f}%"),
        ]

        for column, metric in zip(metrics, metric_data):
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

        # Display each recommended job.
        for index, (_, row) in enumerate(
            results.iterrows(),
            start=1,
        ):
            job_title = safe_text(get_value(row, "job_title"))
            company = safe_text(get_value(row, "company"))
            location = safe_text(get_value(row, "location"))
            experience = safe_text(
                get_value(row, "experience_level")
            )
            description = safe_text(
                get_value(row, "description", "No description available.")
            )

            required_skills = display_skills(
                get_value(row, "skills", "")
            )
            matched_skills = display_skills(
                get_value(row, "matched_skills", None)
            )
            missing_skills = display_skills(
                get_value(row, "missing_skills", None)
            )

            score = format_score(row["match_score"])

            card_html = f"""
            <div class="job-card">
                <div class="job-rank">#{index}</div>

                <div class="job-title">{job_title}</div>
                <div class="job-meta">{company} · {location}</div>

                <div class="score-number">{score:.2f}%</div>
                <div class="score-label">MATCH SCORE</div>

                <div class="score-track">
                    <div class="score-fill"
                         style="width: {score:.2f}%;"></div>
                </div>

                <div class="job-desc">{description}</div>

                <div class="pill-row">
                    <span class="pill">📍 {location}</span>
                    <span class="pill">⚡ {experience}</span>
                    <span class="pill">🎯 Match {score:.2f}%</span>
                </div>

                <div class="skill-grid">
                    <div class="skill-box required">
                        <b>Required Skills</b>
                        {required_skills}
                    </div>

                    <div class="skill-box matched">
                        <b>Matched Skills</b>
                        {matched_skills}
                    </div>

                    <div class="skill-box missing">
                        <b>Missing Skills</b>
                        {missing_skills}
                    </div>
                </div>
            </div>
            """

            st.markdown(
                card_html,
                unsafe_allow_html=True,
            )

        st.success("Job recommendations generated successfully!")

    except Exception as error:
        st.error("An error occurred while generating recommendations.")
        st.exception(error)


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">
        Built using Python · Streamlit · Pandas · TF-IDF ·
        Cosine Similarity · Skill Gap Analysis
    </div>
    """,
    unsafe_allow_html=True,
        )
