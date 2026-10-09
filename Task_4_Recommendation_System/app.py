import html
from textwrap import dedent

import streamlit as st
from recommender import JobRecommender


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Job Recommendation System",
    page_icon="💼",
    layout="wide",
)


def show_html(code):
    """Render trusted HTML/CSS inside Streamlit."""
    st.markdown(
        dedent(code).strip(),
        unsafe_allow_html=True,
    )


def safe_text(value, default="N/A"):
    """Escape text before inserting it into HTML."""
    if value is None:
        return default

    try:
        if value != value:  # Handles NaN
            return default
    except (TypeError, ValueError):
        pass

    return html.escape(str(value))


def format_score(value):
    """Format recommendation score safely."""
    try:
        score = float(value)
        return round(max(0.0, min(100.0, score)), 2)
    except (TypeError, ValueError):
        return 0.0


# =========================================================
# CSS
# =========================================================

show_html("""
<style>
.stApp {
    background:
        radial-gradient(circle at 8% 10%, rgba(37,99,235,.28), transparent 28%),
        radial-gradient(circle at 90% 8%, rgba(236,72,153,.25), transparent 28%),
        radial-gradient(circle at 50% 95%, rgba(16,185,129,.18), transparent 32%),
        linear-gradient(135deg,#dbeafe 0%,#ede9fe 45%,#fce7f3 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1280px;
    padding-top: 30px;
    padding-bottom: 42px;
}

#MainMenu, footer {
    visibility: hidden;
}

/* HERO */

.hero {
    background:
        radial-gradient(circle at 90% 10%,rgba(255,255,255,.22),transparent 24%),
        linear-gradient(135deg,#2563eb 0%,#7c3aed 52%,#ec4899 100%);
    border-radius: 30px;
    padding: 38px;
    color: white;
    box-shadow: 0 25px 65px rgba(124,58,237,.30);
    margin-bottom: 26px;
}

.hero-kicker {
    display: inline-block;
    background: rgba(255,255,255,.18);
    border: 1px solid rgba(255,255,255,.3);
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 900;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(32px,5vw,54px);
    font-weight: 950;
    letter-spacing: -1px;
    line-height: 1.1;
    margin-bottom: 16px;
}

.hero-subtitle {
    font-size: 16px;
    line-height: 1.8;
    color: #f8fafc;
    max-width: 880px;
}

.badge-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 24px;
}

.badge {
    background: rgba(255,255,255,.18);
    color: white;
    border: 1px solid rgba(255,255,255,.3);
    padding: 9px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
}

/* FEATURE CARDS */

.feature-card {
    background: rgba(255,255,255,.95);
    border: 1px solid white;
    border-radius: 24px;
    padding: 23px;
    min-height: 165px;
    box-shadow: 0 16px 42px rgba(15,23,42,.10);
    margin-bottom: 15px;
}

.feature-icon {
    width: 54px;
    height: 54px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    margin-bottom: 15px;
}

.icon-blue {
    background: linear-gradient(135deg,#2563eb,#38bdf8);
}

.icon-purple {
    background: linear-gradient(135deg,#7c3aed,#a855f7);
}

.icon-pink {
    background: linear-gradient(135deg,#ec4899,#f97316);
}

.feature-title {
    color: #111827;
    font-size: 19px;
    font-weight: 900;
    margin-bottom: 8px;
}

.feature-text {
    color: #4b5563;
    font-size: 14px;
    line-height: 1.65;
}

/* SECTION */

.section-title {
    color: #111827;
    font-size: 25px;
    font-weight: 950;
    margin-top: 10px;
    margin-bottom: 16px;
}

/* INPUT AND HELP PANELS */

.input-panel {
    background: rgba(255,255,255,.96);
    border: 1px solid white;
    border-radius: 26px;
    padding: 24px;
    box-shadow: 0 20px 50px rgba(15,23,42,.10);
    margin-bottom: 20px;
}

.help-card {
    background: white;
    color: #374151;
    border: 1px solid #e5e7eb;
    border-radius: 24px;
    padding: 22px;
    line-height: 1.75;
    font-size: 14px;
    box-shadow: 0 15px 35px rgba(15,23,42,.08);
}

.help-title {
    font-size: 20px;
    font-weight: 950;
    color: #111827;
    margin-bottom: 10px;
}

/* METRICS */

.metric-card {
    background: white;
    border-radius: 22px;
    padding: 20px 12px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 15px 35px rgba(15,23,42,.10);
    margin-bottom: 12px;
}

.metric-label {
    color: #6b7280;
    font-size: 12px;
    font-weight: 900;
    margin-bottom: 8px;
}

.metric-value {
    color: #111827;
    font-size: clamp(21px,3vw,32px);
    font-weight: 950;
    overflow-wrap: anywhere;
}

/* JOB CARDS */

.job-card {
    background: white;
    border-radius: 25px;
    padding: 26px 24px 24px 30px;
    margin: 0 0 22px 0;
    border: 1px solid #e5e7eb;
    box-shadow: 0 18px 45px rgba(15,23,42,.12);
    position: relative;
    overflow-wrap: anywhere;
}

.job-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 7px;
    height: 100%;
    background: linear-gradient(180deg,#2563eb,#7c3aed,#ec4899,#10b981);
}

.job-rank {
    float: right;
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    color: white;
    font-weight: 900;
    font-size: 12px;
    padding: 8px 12px;
    border-radius: 999px;
    margin-left: 8px;
}

.job-title {
    color: #111827;
    font-size: clamp(21px,3vw,27px);
    font-weight: 950;
    margin-bottom: 7px;
}

.job-meta {
    color: #2563eb;
    font-size: 14px;
    font-weight: 850;
    margin-bottom: 15px;
}

.job-desc {
    color: #4b5563;
    font-size: 14px;
    line-height: 1.75;
    margin-bottom: 16px;
}

.score-wrap {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}

.score-bar {
    flex: 1;
    height: 10px;
    background: #e5e7eb;
    border-radius: 999px;
    overflow: hidden;
}

.score-fill {
    height: 100%;
    background: linear-gradient(90deg,#2563eb,#7c3aed,#ec4899);
    border-radius: 999px;
}

.score-text {
    color: #7c3aed;
    font-weight: 950;
    font-size: 14px;
    width: 68px;
    text-align: right;
    flex-shrink: 0;
}

.pill-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 15px;
}

.pill {
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
}

.pill-location {
    background: #ecfdf5;
    color: #047857;
}

.pill-exp {
    background: #fff7ed;
    color: #c2410c;
}

.pill-score {
    background: #eef2ff;
    color: #3730a3;
}

/* SKILLS */

.skill-grid {
    display: grid;
    grid-template-columns: repeat(3,minmax(0,1fr));
    gap: 11px;
    margin-top: 14px;
}

.skill-box {
    border-radius: 17px;
    padding: 14px;
    font-size: 13px;
    line-height: 1.65;
    min-width: 0;
    overflow-wrap: anywhere;
}

.skill-box b {
    display: block;
    margin-bottom: 8px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .05em;
}

.required {
    background: linear-gradient(135deg,#eff6ff,#dbeafe);
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
}

.matched {
    background: linear-gradient(135deg,#ecfdf5,#d1fae5);
    color: #047857;
    border: 1px solid #bbf7d0;
}

.missing {
    background: linear-gradient(135deg,#fff7ed,#ffedd5);
    color: #c2410c;
    border: 1px solid #fed7aa;
}

/* EMPTY STATE */

.empty-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 26px;
    padding: 35px 24px;
    text-align: center;
    box-shadow: 0 18px 45px rgba(15,23,42,.10);
}

.empty-icon {
    font-size: 48px;
    margin-bottom: 12px;
}

.empty-title {
    font-size: 23px;
    font-weight: 950;
    color: #111827;
    margin-bottom: 10px;
}

.empty-text {
    color: #4b5563;
    line-height: 1.7;
    margin-bottom: 17px;
}

.sample-chip {
    background: linear-gradient(135deg,#2563eb,#7c3aed,#ec4899);
    color: white;
    display: inline-block;
    padding: 10px 15px;
    border-radius: 999px;
    font-weight: 900;
    font-size: 12px;
}

/* STREAMLIT INPUTS */

.stRadio label,
.stSelectbox label,
.stSlider label,
.stTextArea label {
    color: #111827 !important;
    font-weight: 850 !important;
}

.stTextArea textarea {
    border-radius: 15px !important;
    border: 1px solid #a78bfa !important;
}

div[data-baseweb="select"] > div {
    border-radius: 15px !important;
    border: 1px solid #a78bfa !important;
}

.stButton > button {
    background: linear-gradient(135deg,#2563eb,#7c3aed,#ec4899) !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    padding: 13px 18px !important;
    font-weight: 900 !important;
    width: 100%;
}

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 12px;
    margin-top: 28px;
    padding-bottom: 10px;
}

@media (max-width: 900px) {
    .skill-grid {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 25px;
        border-radius: 23px;
    }

    .input-panel {
        padding: 18px;
    }

    .job-card {
        padding: 23px 16px 20px 23px;
    }
}
</style>
""")


# =========================================================
# LOAD RECOMMENDER
# =========================================================

@st.cache_resource
def load_recommender():
    return JobRecommender()


try:
    recommender = load_recommender()
except Exception as exc:
    st.error(
        "The recommendation engine could not start. "
        "Check that jobs.csv is committed in the "
        "Task_4_Recommendation_System folder."
    )
    st.exception(exc)
    st.stop()


if "recommendations" not in st.session_state:
    st.session_state.recommendations = None


# =========================================================
# HERO
# =========================================================

show_html("""
<div class="hero">
    <div class="hero-kicker">AI-Powered Career Matching</div>

    <div class="hero-title">
        Smart Job Recommendation System
    </div>

    <div class="hero-subtitle">
        Discover suitable job opportunities using your skills,
        preferred location, experience level, and intelligent
        content-based recommendations.
    </div>

    <div class="badge-row">
        <div class="badge">Content-Based Filtering</div>
        <div class="badge">TF-IDF Vectorization</div>
        <div class="badge">Cosine Similarity</div>
        <div class="badge">Skill Gap Analysis</div>
        <div class="badge">Match Scoring</div>
    </div>
</div>
""")


# =========================================================
# FEATURE CARDS
# =========================================================

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    show_html("""
    <div class="feature-card">
        <div class="feature-icon icon-blue">🎯</div>
        <div class="feature-title">Personalized Matching</div>
        <div class="feature-text">
            Finds jobs based on candidate skills, preferred role,
            experience level, and location.
        </div>
    </div>
    """)

with c2:
    show_html("""
    <div class="feature-card">
        <div class="feature-icon icon-purple">📊</div>
        <div class="feature-title">Match Score</div>
        <div class="feature-text">
            Combines skill overlap and text similarity to estimate
            how closely a job matches your profile.
        </div>
    </div>
    """)

with c3:
    show_html("""
    <div class="feature-card">
        <div class="feature-icon icon-pink">🧠</div>
        <div class="feature-title">Skill Gap Analysis</div>
        <div class="feature-text">
            Highlights matching and missing skills to help you
            plan your next learning steps.
        </div>
    </div>
    """)


st.write("")


# =========================================================
# MAIN LAYOUT
# =========================================================

left, right = st.columns([0.9, 1.1], gap="large")


# =========================================================
# CANDIDATE PREFERENCES
# =========================================================

with left:

    show_html(
        '<div class="section-title">Candidate Preferences</div>'
    )

    show_html('<div class="input-panel">')

    mode = st.radio(
        "Recommendation Mode",
        [
            "Recommend by Skills",
            "Recommend by Job Role",
        ],
    )

    top_n = st.slider(
        "Number of recommendations",
        min_value=3,
        max_value=8,
        value=5,
    )

    locations = ["All"] + recommender.get_locations()

    experience_levels = (
        ["All"] + recommender.get_experience_levels()
    )

    location_filter = st.selectbox(
        "Preferred Location",
        locations,
    )

    experience_filter = st.selectbox(
        "Experience Level",
        experience_levels,
    )

    if mode == "Recommend by Skills":

        user_skills = st.text_area(
            "Enter your skills",
            placeholder=(
                "Example: Python, SQL, Pandas, "
                "Machine Learning, HTML, CSS"
            ),
            height=120,
        )

        if st.button(
            "Find Matching Jobs",
            key="find_jobs_by_skills",
        ):

            if not user_skills.strip():

                st.warning(
                    "Please enter at least one skill "
                    "before searching."
                )

            else:

                try:
                    st.session_state.recommendations = (
                        recommender.recommend_by_skills(
                            user_skills,
                            top_n,
                            location_filter,
                            experience_filter,
                        )
                    )

                except Exception as exc:
                    st.error(
                        "Unable to generate skill-based recommendations."
                    )
                    st.exception(exc)

    else:

        selected_job = st.selectbox(
            "Select a job role you like",
            recommender.get_job_titles(),
        )

        selected_details = recommender.get_job_details(
            selected_job
        )

        if selected_details is not None:

            st.info(
                f"Selected Role: "
                f"{selected_details['job_title']}"
            )

            st.write(
                f"**Company:** "
                f"{selected_details['company']}"
            )

            st.write(
                f"**Location:** "
                f"{selected_details['location']}"
            )

            st.write(
                f"**Experience:** "
                f"{selected_details['experience_level']}"
            )

            st.write(
                f"**Required Skills:** "
                f"{selected_details['skills']}"
            )

            st.write(
                selected_details["description"]
            )

        if st.button(
            "Find Similar Jobs",
            key="find_jobs_by_role",
        ):

            try:
                st.session_state.recommendations = (
                    recommender.recommend_by_job_title(
                        selected_job,
                        top_n,
                        location_filter,
                        experience_filter,
                    )
                )

            except Exception as exc:
                st.error(
                    "Unable to generate role-based recommendations."
                )
                st.exception(exc)

    show_html("</div>")

    show_html("""
    <div class="help-card">
        <div class="help-title">⚙️ How the engine works</div>

        The system combines job titles, required skills,
        experience levels, locations, and descriptions.
        TF-IDF converts job information into numerical vectors.
        Cosine similarity compares textual features, while
        skill-gap analysis identifies skills that may need
        improvement. Location and experience filters narrow
        the results.
    </div>
    """)


# =========================================================
# RECOMMENDATION RESULTS
# =========================================================

with right:

    show_html(
        '<div class="section-title">Recommended Jobs</div>'
    )

    recommendations = st.session_state.recommendations

    if recommendations is None:

        show_html("""
        <div class="empty-card">
            <div class="empty-icon">🔍</div>
            <div class="empty-title">No recommendations yet</div>
            <div class="empty-text">
                Enter your skills or choose a job role,
                then click the recommendation button.
            </div>
            <div class="sample-chip">
                Try: Python, SQL, Machine Learning
            </div>
        </div>
        """)

    elif recommendations.empty:

        st.warning(
            "No matching jobs found. Try changing your skills, "
            "location, or experience level."
        )

    else:

        # Check the expected columns
        if "match_score" not in recommendations.columns:

            st.error(
                "The recommendation engine did not return "
                "the required match_score column. "
                "Check recommender.py."
            )
            st.stop()

        result_count = len(recommendations)

        avg_score = round(
            recommendations["match_score"].apply(
                format_score
            ).mean(),
            2,
        )

        best_score = round(
            recommendations["match_score"].apply(
                format_score
            ).max(),
            2,
        )

        m1, m2, m3 = st.columns(3)

        with m1:
            show_html(f"""
            <div class="metric-card">
                <div class="metric-label">RESULTS</div>
                <div class="metric-value">{result_count}</div>
            </div>
            """)

        with m2:
            show_html(f"""
            <div class="metric-card">
                <div class="metric-label">AVG MATCH</div>
                <div class="metric-value">{avg_score}%</div>
            </div>
            """)

        with m3:
            show_html(f"""
            <div class="metric-card">
                <div class="metric-label">BEST MATCH</div>
                <div class="metric-value">{best_score}%</div>
            </div>
            """)

        st.write("")

        # Render each recommendation as an HTML job card
        for rank, (_, row) in enumerate(
            recommendations.iterrows(),
            start=1,
        ):

            score = format_score(row.get("match_score", 0))

            job_title = safe_text(
                row.get("job_title")
            )

            company = safe_text(
                row.get("company")
            )

            location = safe_text(
                row.get("location")
            )

            experience = safe_text(
                row.get("experience_level")
            )

            description = safe_text(
                row.get("description")
            )

            required_skills = safe_text(
                row.get("skills")
            )

            matched_skills = safe_text(
                row.get("matched_skills", "N/A")
            )

            missing_skills = safe_text(
                row.get("missing_skills", "N/A")
            )

            show_html(f"""
            <div class="job-card">

                <div class="job-rank">#{rank}</div>

                <div class="job-title">
                    {job_title}
                </div>

                <div class="job-meta">
                    {company} · {location}
                </div>

                <div class="score-wrap">
                    <div class="score-bar">
                        <div
                            class="score-fill"
                            style="width: {score}%"
                        ></div>
                    </div>

                    <div class="score-text">
                        {score:.2f}%
                    </div>
                </div>

                <div class="job-desc">
                    {description}
                </div>

                <div class="pill-row">
                    <span class="pill pill-location">
                        📍 {location}
                    </span>

                    <span class="pill pill-exp">
                        ⚡ {experience}
                    </span>

                    <span class="pill pill-score">
                        Match {score:.2f}%
                    </span>
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
            """)


# =========================================================
# FOOTER
# =========================================================

show_html("""
<div class="footer">
    Built using Python · Streamlit · Pandas · TF-IDF ·
    Cosine Similarity · Skill Gap Analysis
</div>
""")
