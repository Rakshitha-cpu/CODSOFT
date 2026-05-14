import streamlit as st
from PIL import Image
from image_captioning import ImageCaptionGenerator
import datetime

st.set_page_config(
    page_title="VisionCaption AI",
    page_icon="🖼️",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, rgba(37,99,235,0.14), transparent 30%),
        radial-gradient(circle at bottom right, rgba(236,72,153,0.16), transparent 30%),
        linear-gradient(135deg, #f8fafc 0%, #eef2ff 48%, #fdf2f8 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1180px;
    padding-top: 32px;
    padding-bottom: 36px;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 30px;
    padding: 34px;
    box-shadow: 0 24px 60px rgba(15, 23, 42, 0.10);
    margin-bottom: 26px;
}

.hero-title {
    font-size: 48px;
    font-weight: 950;
    color: #111827;
    margin-bottom: 10px;
}

.gradient-text {
    background: linear-gradient(135deg, #2563eb, #7c3aed, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #4b5563;
    font-size: 16px;
    line-height: 1.7;
    max-width: 850px;
}

.badge-row {
    margin-top: 22px;
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.badge {
    background: #eef2ff;
    color: #3730a3;
    border: 1px solid #c7d2fe;
    padding: 8px 13px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 900;
}

.section-title {
    color: #111827;
    font-size: 22px;
    font-weight: 950;
    margin-bottom: 14px;
}

.caption-main {
    background: linear-gradient(135deg, #2563eb, #7c3aed, #ec4899);
    color: white;
    padding: 24px;
    border-radius: 22px;
    font-size: 21px;
    font-weight: 900;
    line-height: 1.6;
    box-shadow: 0 18px 40px rgba(124, 58, 237, 0.25);
    margin-bottom: 16px;
}

.result-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 18px;
    line-height: 1.65;
    box-shadow: 0 10px 28px rgba(15,23,42,0.06);
    margin-bottom: 14px;
}

.warning-box {
    background: #fff7ed;
    color: #9a3412;
    border: 1px solid #fed7aa;
    padding: 15px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.6;
    margin-top: 14px;
}

.info-box {
    background: white;
    color: #374151;
    border: 1px solid #e5e7eb;
    padding: 18px;
    border-radius: 18px;
    line-height: 1.7;
    font-size: 15px;
    box-shadow: 0 10px 26px rgba(15,23,42,0.06);
}

.stButton > button {
    background: linear-gradient(135deg, #2563eb, #7c3aed) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 13px 18px !important;
    font-weight: 950 !important;
    width: 100%;
    box-shadow: 0 14px 32px rgba(37, 99, 235, 0.20);
}

.stButton > button:hover {
    transform: translateY(-2px);
    color: white !important;
}

.stDownloadButton > button {
    background: #111827 !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 13px 18px !important;
    font-weight: 950 !important;
    width: 100%;
}

[data-testid="stFileUploader"] {
    background: white;
    border-radius: 18px;
    padding: 14px;
    border: 1px dashed #a5b4fc;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 10px 26px rgba(15,23,42,0.06);
}

.footer-text {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "caption_history" not in st.session_state:
    st.session_state.caption_history = []

if "caption_candidates" not in st.session_state:
    st.session_state.caption_candidates = []

if "final_caption" not in st.session_state:
    st.session_state.final_caption = ""

if "last_uploaded_name" not in st.session_state:
    st.session_state.last_uploaded_name = None


# ---------------- MODEL ----------------

@st.cache_resource
def load_caption_model():
    return ImageCaptionGenerator()


# ---------------- HELPERS ----------------

def create_detailed_caption(caption):
    return (
        f"This image appears to show {caption}. "
        "The caption is generated using a transformer-based vision-language model."
    )


def create_social_caption(caption):
    return f"{caption.capitalize()} ✨ #AI #ImageCaptioning #ComputerVision"


def add_to_history(file_name, caption):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
    st.session_state.caption_history.append(
        {
            "file": file_name,
            "caption": caption,
            "time": timestamp
        }
    )


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <div class="hero-title">🖼️ <span class="gradient-text">VisionCaption AI</span></div>
    <div class="hero-subtitle">
        Upload an image and generate natural language captions using a pre-trained transformer-based vision-language model.
        Review and edit the final caption before downloading it.
    </div>
    <div class="badge-row">
        <div class="badge">Computer Vision</div>
        <div class="badge">NLP</div>
        <div class="badge">Transformer Model</div>
        <div class="badge">Caption Suggestions</div>
        <div class="badge">Human Review</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN LAYOUT ----------------

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="section-title">Upload Image</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        if uploaded_file.name != st.session_state.last_uploaded_name:
            st.session_state.caption_candidates = []
            st.session_state.final_caption = ""
            st.session_state.last_uploaded_name = uploaded_file.name

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image Preview",
            width="stretch"
        )

        img_width, img_height = image.size
        image_format = image.format if image.format else "N/A"

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("Width", img_width)

        with m2:
            st.metric("Height", img_height)

        with m3:
            st.metric("Format", image_format)

        st.markdown("""
        <div class="warning-box">
            AI captions may be inaccurate for unclear images, hand gestures, small objects, or low lighting.
            Select the best suggestion and edit the final caption if needed.
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="info-box">
            Upload a JPG, JPEG, or PNG image. The model will analyze the image and generate caption suggestions.
        </div>
        """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-title">Generated Caption</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        if st.button("Generate Caption Suggestions"):
            with st.spinner("Generating captions..."):
                caption_model = load_caption_model()
                candidates = caption_model.generate_caption_candidates(image)

            st.session_state.caption_candidates = candidates
            st.session_state.final_caption = candidates[0] if candidates else ""

        if st.session_state.caption_candidates:
            selected_caption = st.radio(
                "Select best caption",
                st.session_state.caption_candidates
            )

            st.session_state.final_caption = st.text_area(
                "Edit final caption",
                value=selected_caption,
                height=100
            )

            final_caption = st.session_state.final_caption

            st.markdown(
                f'<div class="caption-main">"{final_caption.capitalize()}"</div>',
                unsafe_allow_html=True
            )

            detailed_caption = create_detailed_caption(final_caption)
            social_caption = create_social_caption(final_caption)

            st.markdown(
                f'<div class="result-card"><b>Detailed Caption</b><br>{detailed_caption}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="result-card"><b>Social Media Caption</b><br>{social_caption}</div>',
                unsafe_allow_html=True
            )

            captions_text = (
                "Image Captioning Result\n\n"
                f"Caption Suggestions:\n"
                + "\n".join([f"- {c}" for c in st.session_state.caption_candidates])
                + "\n\n"
                f"Final Caption: {final_caption}\n\n"
                f"Detailed Caption: {detailed_caption}\n\n"
                f"Social Media Caption: {social_caption}\n"
            )

            c1, c2 = st.columns(2)

            with c1:
                st.download_button(
                    label="Download Captions",
                    data=captions_text,
                    file_name="generated_caption.txt",
                    mime="text/plain"
                )

            with c2:
                if st.button("Save to History"):
                    add_to_history(uploaded_file.name, final_caption)
                    st.success("Saved.")

    else:
        st.markdown("""
        <div class="info-box">
            Caption suggestions will appear here after image upload and generation.
        </div>
        """, unsafe_allow_html=True)

# ---------------- HISTORY ----------------

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">Caption History</div>', unsafe_allow_html=True)

if len(st.session_state.caption_history) == 0:
    st.markdown("""
    <div class="info-box">
        No captions saved yet.
    </div>
    """, unsafe_allow_html=True)
else:
    for item in reversed(st.session_state.caption_history[-5:]):
        st.markdown(
            f"""
            <div class="result-card">
                <b>File:</b> {item["file"]}<br>
                <b>Final Caption:</b> {item["caption"]}<br>
                <b>Time:</b> {item["time"]}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="footer-text">Built using Python, Streamlit, Transformers, and a pre-trained BLIP image captioning model</div>',
    unsafe_allow_html=True
)