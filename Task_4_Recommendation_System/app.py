import streamlit as st
from recommender import JobRecommender
from textwrap import dedent

st.set_page_config(
    page_title="Smart Job Recommendation System",
    page_icon="💼",
    layout="wide"
)

def show_html(code):
    st.markdown(dedent(code).strip(), unsafe_allow_html=True)

# ---------------- CSS ----------------

show_html("""
<style>
.stApp {
    background:
        radial-gradient(circle at 8% 10%, rgba(37, 99, 235, 0.35), transparent 28%),
        radial-gradient(circle at 90% 8%, rgba(236, 72, 153, 0.32), transparent 28%),
        radial-gradient(circle at 50% 95%, rgba(16, 185, 129, 0.25), transparent 32%),
        linear-gradient(135deg, #dbeafe 0%, #ede9fe 45%, #fce7f3 100%);
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
        radial-gradient(circle at 90% 10%, rgba(255,255,255,0.22), transparent 24%),
        linear-gradient(135deg, #2563eb 0%, #7c3aed 52%, #ec4899 100%);
    border-radius: 36px;
    padding: 42px;
    color: white;
    box-shadow: 0 34px 90px rgba(124, 58, 237, 0.38);
    margin-bottom: 26px;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    right: -70px;
    bottom: -90px;
    background: rgba(255,255,255,0.16);
    border-radius: 50%;
}

.hero-kicker {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.30);
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 900;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 54px;
    font-weight: 950;
    letter-spacing: -1.4px;
    line-height: 1.05;
    margin-bottom: 16px;
    max-width: 900px;
}

.hero-subtitle {
    font-size: 17px;
    line-height: 1.75;
    color: #f8fafc;
    max-width: 880px;
}

.badge-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 25px;
}

.badge {
    background: rgba(255,255,255,0.20);
    color: white;
    border: 1px solid rgba(255,255,255,0.32);
    padding: 9px 15px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 900;
}

/* FEATURE CARDS */

.feature-card {
    background: rgba(255,255,255,0.92);
    border: 1px solid rgba(255,255,255,0.92);
    border-radius: 28px;
    padding: 24px;
    min-height: 160px;
    box-shadow: 0 22px 55px rgba(15, 23, 42, 0.12);
    transition: 0.25s ease;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(37,99,235,0.08), rgba(236,72,153,0.08));
    opacity: 0;
    transition: 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 32px 75px rgba(15, 23, 42, 0.18);
}

.feature-card:hover::before {
    opacity: 1;
}

.feature-icon {
    width: 58px;
    height: 58px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    color: white;
    margin-bottom: 16px;
    position: relative;
}

.icon-blue {
    background: linear-gradient(135deg, #2563eb, #38bdf8);
}

.icon-purple {
    background: linear-gradient(135deg, #7c3aed, #a855f7);
}

.icon-pink {
    background: linear-gradient(135deg, #ec4899, #f97316);
}

.feature-title {
    color: #111827;
    font-size: 20px;
    font-weight: 950;
    margin-bottom: 8px;
    position: relative;
}

.feature-text {
    color: #4b5563;
    font-size: 14px;
    line-height: 1.65;
    position: relative;
}

/* SECTION */

.section-title {
    color: #111827;
    font-size: 26px;
    font-weight: 950;
    margin-top: 12px;
    margin-bottom: 15px;
}

/* INPUT PANEL */

.input-panel {
    background: rgba(255,255,255,0.94);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 30px;
    padding: 26px;
    box-shadow: 0 26px 65px rgba(15,23,42,0.13);
    margin-bottom: 20px;
}

.help-card {
    background:
        linear-gradient(135deg, rgba(255,255,255,0.96), rgba(248,250,252,0.96));
    color: #374151;
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 26px;
    padding: 22px;
    line-height: 1.7;
    font-size: 15px;
    box-shadow: 0 18px 45px rgba(15,23,42,0.10);
}

.help-title {
    font-size: 21px;
    font-weight: 950;
    color: #111827;
    margin-bottom: 10px;
}

/* METRIC CARDS */

.metric-card {
    background: white;
    border-radius: 26px;
    padding: 22px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 20px 52px rgba(15,23,42,0.13);
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: "";
    position: absolute;
    height: 6px;
    left: 0;
    top: 0;
    right: 0;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #ec4899);
}

.metric-label {
    color: #6b7280;
    font-size: 13px;
    font-weight: 950;
    margin-bottom: 8px;
}

.metric-value {
    color: #111827;
    font-size: 34px;
    font-weight: 950;
}

/* JOB CARD */

.job-card {
    background: white;
    border-radius: 30px;
    padding: 28px 26px 26px 34px;
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.95);
    box-shadow: 0 25px 65px rgba(15,23,42,0.14);
    position: relative;
    overflow: hidden;
    transition: 0.25s ease;
}

.job-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 36px 85px rgba(15,23,42,0.20);
}

.job-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 9px;
    height: 100%;
    background: linear-gradient(180deg, #2563eb, #7c3aed, #ec4899, #10b981);
}

.job-rank {
    position: absolute;
    top: 20px;
    right: 22px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    font-weight: 950;
    font-size: 13px;
    padding: 8px 13px;
    border-radius: 999px;
}

.job-title {
    color: #111827;
    font-size: 27px;
    font-weight: 950;
    margin-bottom: 7px;
    padding-right: 80px;
}

.job-meta {
    color: #2563eb;
    font-size: 14px;
    font-weight: 900;
    margin-bottom: 14px;
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
    height: 11px;
    background: #e5e7eb;
    border-radius: 999px;
    overflow: hidden;
}

.score-fill {
    height: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed, #ec4899);
    border-radius: 999px;
}

.score-text {
    color: #7c3aed;
    font-weight: 950;
    font-size: 15px;
    width: 65px;
    text-align: right;
}

.pill-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 15px;
}

.pill {
    padding: 8px 13px;
    border-radius: 999px;
    font-size: 13px;
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

.skill-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 14px;
}

.skill-box {
    border-radius: 20px;
    padding: 15px;
    font-size: 13px;
    line-height: 1.55;
    min-height: 120px;
}

.skill-box b {
    display: block;
    margin-bottom: 8px;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.required {
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
}

.matched {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
    color: #047857;
    border: 1px solid #bbf7d0;
}

.missing {
    background: linear-gradient(135deg, #fff7ed, #ffedd5);
    color: #c2410c;
    border: 1px solid #fed7aa;
}

/* EMPTY */

.empty-card {
    background: white;
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 30px;
    padding: 42px;
    text-align: center;
    box-shadow: 0 24px 62px rgba(15,23,42,0.13);
}

.empty-icon {
    font-size: 54px;
    margin-bottom: 14px;
}

.empty-title {
    font-size: 26px;
    font-weight: 950;
    color: #111827;
    margin-bottom: 10px;
}

.empty-text {
    color: #4b5563;
    line-height: 1.7;
    margin-bottom: 18px;
}

.sample-chip {
    background: linear-gradient(135deg, #2563eb, #7c3aed, #ec4899);
    color: white;
    display: inline-block;
    padding: 11px 18px;
    border-radius: 999px;
    font-weight: 900;
    font-size: 13px;
}

/* STREAMLIT WIDGETS */

.stRadio label,
.stSelectbox label,
.stSlider label,
.stTextArea label {
    color: #111827 !important;
    font-weight: 900 !important;
}

[data-testid="stRadio"] label p {
    color: #111827 !important;
    font-weight: 700 !important;
}

.stTextArea textarea {
    border-radius: 18px !important;
    border: 1px solid #a78bfa !important;
    box-shadow: 0 10px 25px rgba(124,58,237,0.12);
}

div[data-baseweb="select"] > div {
    border-radius: 18px !important;
    border: 1px solid #a78bfa !important;
    box-shadow: 0 10px 25px rgba(124,58,237,0.12);
}

.stButton > button {
    background: linear-gradient(135deg, #2563eb, #7c3aed, #ec4899) !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    padding: 15px 20px !important;
    font-weight: 950 !important;
    width: 100%;
    box-shadow: 0 18px 42px rgba(124,58,237,0.34);
    transition: 0.22s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 25px 55px rgba(124,58,237,0.45);
}

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    margin-top: 30px;
}

@media (max-width: 900px) {
    .skill-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""")

# ---------------- LOAD ----------------

@st.cache_resource
def load_recommender():
    return JobRecommender()

recommender = load_recommender()

if "recommendations" not in st.session_state:
    st.session_state.recommendations = None

# ---------------- HERO ----------------

show_html("""
<div class="hero">
    <div class="hero-kicker">AI-Powered Career Matching</div>
    <div class="hero-title">Smart Job Recommendation System</div>
    <div class="hero-subtitle">
        A colorful HR-tech dashboard that recommends suitable job roles using candidate skills,
        experience level, preferred location, TF-IDF vectorization, cosine similarity, and skill gap analysis.
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

# ---------------- FEATURE CARDS ----------------

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    show_html("""
    <div class="feature-card">
        <div class="feature-icon icon-blue">🎯</div>
        <div class="feature-title">Personalized Matching</div>
        <div class="feature-text">
            Finds jobs based on candidate skills, preferred role, experience level, and location.
        </div>
    </div>
    """)

with c2:
    show_html("""
    <div class="feature-card">
        <div class="feature-icon icon-purple">📊</div>
        <div class="feature-title">Match Score</div>
        <div class="feature-text">
            Calculates similarity between candidate profile and job requirements using cosine similarity.
        </div>
    </div>
    """)

with c3:
    show_html("""
    <div class="feature-card">
        <div class="feature-icon icon-pink">🧠</div>
        <div class="feature-title">Skill Gap Analysis</div>
        <div class="feature-text">
            Shows matched skills and missing skills so candidates know what to improve.
        </div>
    </div>
    """)

st.write("")

# ---------------- LAYOUT ----------------

left, right = st.columns([0.9, 1.1], gap="large")

with left:
    show_html('<div class="section-title">Candidate Preferences</div>')
    show_html('<div class="input-panel">')

    mode = st.radio(
        "Recommendation Mode",
        ["Recommend by Skills", "Recommend by Job Role"]
    )

    top_n = st.slider(
        "Number of recommendations",
        min_value=3,
        max_value=8,
        value=5
    )

    locations = ["All"] + recommender.get_locations()
    experience_levels = ["All"] + recommender.get_experience_levels()

    location_filter = st.selectbox("Preferred Location", locations)
    experience_filter = st.selectbox("Experience Level", experience_levels)

    if mode == "Recommend by Skills":
        user_skills = st.text_area(
            "Enter your skills",
            placeholder="Example: Python SQL Machine Learning",
            height=120
        )

        if st.button("Find Matching Jobs"):
            st.session_state.recommendations = recommender.recommend_by_skills(
                user_skills,
                top_n,
                location_filter,
                experience_filter
            )

    else:
        selected_job = st.selectbox(
            "Select a job role you like",
            recommender.get_job_titles()
        )

        selected_details = recommender.get_job_details(selected_job)

        if selected_details is not None:
            st.info(f"Selected Role: {selected_details['job_title']}")
            st.write(f"**Company:** {selected_details['company']}")
            st.write(f"**Location:** {selected_details['location']}")
            st.write(f"**Experience:** {selected_details['experience_level']}")
            st.write(f"**Required Skills:** {selected_details['skills']}")
            st.write(selected_details["description"])

        if st.button("Find Similar Jobs"):
            st.session_state.recommendations = recommender.recommend_by_job_title(
                selected_job,
                top_n,
                location_filter,
                experience_filter
            )

    show_html('</div>')

    show_html("""
    <div class="help-card">
        <div class="help-title">⚙️ How the engine works</div>
        The system combines job title, required skills, experience level, location, and job description.
        TF-IDF converts the text into numerical vectors. Cosine similarity compares jobs and returns
        the closest matches. Skill gap analysis shows matched and missing skills.
    </div>
    """)

with right:
    show_html('<div class="section-title">Recommended Jobs</div>')

    recommendations = st.session_state.recommendations

    if recommendations is None:
        show_html("""
        <div class="empty-card">
            <div class="empty-icon">🔍</div>
            <div class="empty-title">No recommendations yet</div>
            <div class="empty-text">
                Enter your skills or choose a job role, then click the recommendation button.
            </div>
            <div class="sample-chip">Try: Python SQL Machine Learning</div>
        </div>
        """)

    elif recommendations.empty:
        st.warning("No matching jobs found. Try changing location, experience level, or skills.")

    else:
        result_count = len(recommendations)
        avg_score = round(recommendations["match_score"].mean(), 2)
        best_score = round(recommendations["match_score"].max(), 2)

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

        for rank, (_, row) in enumerate(recommendations.iterrows(), start=1):
            score = float(row["match_score"])
            score_width = max(min(score, 100), 0)

            show_html(f"""
            <div class="job-card">
                <div class="job-rank">#{rank}</div>
                <div class="job-title">{row["job_title"]}</div>
                <div class="job-meta">{row["company"]} · {row["location"]}</div>

                <div class="score-wrap">
                    <div class="score-bar">
                        <div class="score-fill" style="width: {score_width}%"></div>
                    </div>
                    <div class="score-text">{score}%</div>
                </div>

                <div class="job-desc">{row["description"]}</div>

                <div class="pill-row">
                    <span class="pill pill-location">📍 {row["location"]}</span>
                    <span class="pill pill-exp">⚡ {row["experience_level"]}</span>
                    <span class="pill pill-score">Match {row["match_score"]}%</span>
                </div>

                <div class="skill-grid">
                    <div class="skill-box required">
                        <b>Required Skills</b>
                        {row["skills"]}
                    </div>
                    <div class="skill-box matched">
                        <b>Matched Skills</b>
                        {row.get("matched_skills", "N/A")}
                    </div>
                    <div class="skill-box missing">
                        <b>Missing Skills</b>
                        {row.get("missing_skills", "N/A")}
                    </div>
                </div>
            </div>
            """)

# ---------------- FOOTER ----------------

show_html("""
<div class="footer">
    Built using Python · Streamlit · Pandas · TF-IDF · Cosine Similarity · Skill Gap Analysis
</div>
""")