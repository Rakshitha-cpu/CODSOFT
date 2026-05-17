import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import json
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="FaceVision AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- PATHS ----------------

DATASET_DIR = "dataset"
MODEL_DIR = "trained_model"
LOG_DIR = "attendance_logs"

MODEL_PATH = os.path.join(MODEL_DIR, "face_model.yml")
LABEL_PATH = os.path.join(MODEL_DIR, "labels.json")
LOG_PATH = os.path.join(LOG_DIR, "recognition_log.csv")

os.makedirs(DATASET_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ---------------- STYLE ----------------

st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Segoe UI", Arial, sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 12% 18%, rgba(0,212,170,0.16), transparent 22%),
            radial-gradient(circle at 82% 12%, rgba(56,189,248,0.16), transparent 20%),
            radial-gradient(circle at 78% 82%, rgba(167,139,250,0.14), transparent 20%),
            linear-gradient(135deg, #030712 0%, #0b1020 45%, #111827 100%);
        color: #e5e7eb;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1520px;
        padding-top: 1rem;
        padding-bottom: 1.8rem;
    }

    .glass {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 20px 60px rgba(0,0,0,0.30);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 28px;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 2rem;
    }

    .hero::before, .hero::after {
        content: "";
        position: absolute;
        border-radius: 999px;
        filter: blur(30px);
        opacity: 0.95;
        animation: floaty 7s ease-in-out infinite;
        pointer-events: none;
    }

    .hero::before {
        width: 220px;
        height: 220px;
        background: rgba(0,212,170,0.20);
        top: -60px;
        right: 5%;
    }

    .hero::after {
        width: 180px;
        height: 180px;
        background: rgba(56,189,248,0.18);
        bottom: -55px;
        left: 8%;
        animation-delay: 1.2s;
    }

    @keyframes floaty {
        0%,100% { transform: translateY(0px) translateX(0px) scale(1); }
        50% { transform: translateY(-14px) translateX(8px) scale(1.05); }
    }

    .brand {
        font-size: 3.65rem;
        font-weight: 950;
        line-height: 0.98;
        letter-spacing: -0.06em;
        margin: 0;
        background: linear-gradient(135deg, #00d4aa 0%, #38bdf8 38%, #a78bfa 72%, #fb7185 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 28px rgba(56,189,248,0.12);
    }

    .subtext {
        margin-top: 0.8rem;
        color: rgba(226,232,240,0.82);
        font-size: 1.03rem;
        line-height: 1.85;
        max-width: 1020px;
    }

    .chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 1.1rem;
    }

    .chip {
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.13);
        color: #f8fafc;
        font-size: 0.84rem;
        font-weight: 700;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 950;
        letter-spacing: -0.04em;
        color: #f8fafc;
        margin-bottom: 0.55rem;
    }

    .section-subtitle {
        color: rgba(226,232,240,0.70);
        font-size: 0.94rem;
        line-height: 1.65;
        margin-bottom: 0.9rem;
    }

    .glass-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.05));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 24px;
        padding: 1rem 1rem;
        box-shadow: 0 16px 42px rgba(0,0,0,0.22);
    }

    .feature-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05));
        border: 1px solid rgba(255,255,255,0.13);
        border-left: 4px solid rgba(0,212,170,0.95);
        border-radius: 22px;
        padding: 1rem;
        color: #f8fafc;
        box-shadow: 0 16px 40px rgba(0,0,0,0.20);
        line-height: 1.7;
    }

    .feature-card b, .feature-card strong {
        color: #ffffff;
    }

    .tiny-label {
        font-size: 0.78rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        font-weight: 800;
        color: rgba(226,232,240,0.64);
        margin-bottom: 0.3rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #00d4aa 0%, #38bdf8 45%, #a78bfa 100%) !important;
        color: #03111d !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 0.9rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
        box-shadow: 0 16px 38px rgba(0,212,170,0.18);
        transition: all 0.22s ease-in-out;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 22px 48px rgba(56,189,248,0.28);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(3,7,18,0.96), rgba(15,23,42,0.96));
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    [data-testid="stSidebar"] .stRadio > div {
        background: rgba(255,255,255,0.05);
        padding: 10px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stMetric"] {
        background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 22px;
        padding: 16px;
        box-shadow: 0 16px 36px rgba(0,0,0,0.20);
    }

    [data-testid="stMetric"] label, [data-testid="stMetric"] div {
        color: #f8fafc !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 26px;
        box-shadow: 0 18px 44px rgba(0,0,0,0.22);
    }

    [data-testid="stDataFrame"] {
        background: rgba(255,255,255,0.96);
        border-radius: 18px;
        overflow: hidden;
    }

    .footer-note {
        text-align: center;
        color: rgba(226,232,240,0.58);
        font-size: 13px;
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- FACE DETECTOR ----------------

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- HELPERS ----------------

def pil_to_cv2(image):
    image = image.convert("RGB")
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


def cv2_to_pil(image):
    return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def detect_faces(image_bgr):
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60, 60)
    )

    return faces, gray


def save_face_image(person_name, image_bgr):
    person_name = person_name.strip().replace(" ", "_")

    if not person_name:
        return False, "Name cannot be empty."

    faces, gray = detect_faces(image_bgr)

    if len(faces) == 0:
        return False, "No face detected. Use a clearer front-facing image."

    person_dir = os.path.join(DATASET_DIR, person_name)
    os.makedirs(person_dir, exist_ok=True)

    saved_count = 0

    for (x, y, w, h) in faces:
        face_roi = cv2.resize(gray[y:y+h, x:x+w], (200, 200))

        augmented_faces = [
            face_roi,
            cv2.flip(face_roi, 1),
            cv2.convertScaleAbs(face_roi, alpha=1.15, beta=25),
            cv2.convertScaleAbs(face_roi, alpha=0.90, beta=-20),
            cv2.convertScaleAbs(face_roi, alpha=1.35, beta=0),
            cv2.equalizeHist(face_roi)
        ]

        for aug_face in augmented_faces:
            file_name = f"{person_name}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"
            cv2.imwrite(os.path.join(person_dir, file_name), aug_face)
            saved_count += 1

    return True, f"{saved_count} face samples saved for {person_name}."


def train_model():
    faces = []
    labels = []
    label_map = {}
    current_label = 0

    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
    except Exception:
        return False, "OpenCV face module missing. Install opencv-contrib-python."

    for person_name in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person_name)

        if not os.path.isdir(person_path):
            continue

        image_files = os.listdir(person_path)

        if not image_files:
            continue

        label_map[current_label] = person_name

        for image_name in image_files:
            image_path = os.path.join(person_path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if image is None:
                continue

            faces.append(cv2.resize(image, (200, 200)))
            labels.append(current_label)

        current_label += 1

    if not faces:
        return False, "No training images found. Enroll at least one face first."

    recognizer.train(faces, np.array(labels))
    recognizer.save(MODEL_PATH)

    with open(LABEL_PATH, "w") as file:
        json.dump(label_map, file)

    return True, f"Model trained successfully with {len(faces)} samples."


def load_model():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(LABEL_PATH):
        return None, None

    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
    except Exception:
        return None, None

    recognizer.read(MODEL_PATH)

    with open(LABEL_PATH, "r") as file:
        label_map = {int(k): v for k, v in json.load(file).items()}

    return recognizer, label_map


def log_recognition(name, confidence):
    now = datetime.now()

    row = {
        "Name": name,
        "Confidence": confidence,
        "Date": now.strftime("%d-%m-%Y"),
        "Time": now.strftime("%I:%M:%S %p")
    }

    if os.path.exists(LOG_PATH):
        df = pd.read_csv(LOG_PATH)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(LOG_PATH, index=False)


def recognize_faces(image_bgr, threshold=90):
    recognizer, label_map = load_model()

    if recognizer is None:
        return None, "Model not trained yet. Please train the model first."

    faces, gray = detect_faces(image_bgr)
    output = image_bgr.copy()
    results = []

    if len(faces) == 0:
        return output, "No faces detected."

    for (x, y, w, h) in faces:
        face_roi = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
        label, confidence = recognizer.predict(face_roi)

        if confidence < threshold:
            name = label_map.get(label, "Unknown")
            color = (0, 212, 170)
        else:
            name = "Unknown"
            color = (56, 189, 248)

        confidence_score = round(max(0, 100 - confidence), 2)

        cv2.rectangle(output, (x, y), (x+w, y+h), color, 3)
        cv2.rectangle(output, (x, y-36), (x+w, y), color, -1)

        cv2.putText(
            output,
            f"{name} ({confidence_score}%)",
            (x+8, y-11),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.72,
            (255, 255, 255),
            2
        )

        results.append(
            {
                "Name": name,
                "Confidence": confidence_score,
                "Raw LBPH Distance": round(confidence, 2)
            }
        )

        if name != "Unknown":
            log_recognition(name, confidence_score)

    return output, results


def get_dataset_summary():
    people = []

    for person_name in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person_name)

        if os.path.isdir(person_path):
            people.append(
                {
                    "Name": person_name,
                    "Images": len(os.listdir(person_path))
                }
            )

    return pd.DataFrame(people)


def get_recent_logs():
    if os.path.exists(LOG_PATH):
        return pd.read_csv(LOG_PATH).tail(12)

    return pd.DataFrame()


# ---------------- SESSION ----------------

if "recognized_image" not in st.session_state:
    st.session_state.recognized_image = None

if "recognition_results" not in st.session_state:
    st.session_state.recognition_results = None

dataset_df = get_dataset_summary()
registered_people = len(dataset_df)
total_images = int(dataset_df["Images"].sum()) if not dataset_df.empty else 0
model_status = "Trained" if os.path.exists(MODEL_PATH) else "Not Trained"
recent_logs_df = get_recent_logs()

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 FaceVision AI")
    st.caption("Neon glassmorphism studio")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Navigation")

    nav = st.radio(
        "",
        ["Dashboard", "Enroll", "Train", "Recognize", "Logs"],
        label_visibility="collapsed"
    )

    st.markdown("### Recognition Settings")

    threshold = st.slider(
        "Threshold",
        min_value=40,
        max_value=120,
        value=90,
        help="Higher threshold is less strict. Try 90–105 if your face is not recognized."
    )

    st.markdown("### Quick Stats")
    st.metric("People", registered_people)
    st.metric("Samples", total_images)
    st.metric("Model", model_status)

    st.markdown("### Pro Tips")
    st.caption("Use bright front-facing images.")
    st.caption("Add multiple samples for each person.")
    st.caption("Train the model after enrollment.")

# ---------------- HERO ----------------

st.markdown(
    """
    <div class="glass hero">
        <div class="brand">FaceVision AI</div>
        <div class="subtext">
            A futuristic face enrollment, training, and recognition experience designed to feel premium, bold, and unforgettable.
            Built with Streamlit and OpenCV, styled with cinematic glassmorphism and bright neon accents.
        </div>
        <div class="chip-row">
            <span class="chip">Glassmorphism UI</span>
            <span class="chip">Neon Gradient</span>
            <span class="chip">Face Detection</span>
            <span class="chip">Face Recognition</span>
            <span class="chip">Attendance Logs</span>
            <span class="chip">Premium Dashboard</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- METRICS ----------------

m1, m2, m3, m4 = st.columns(4)

m1.metric("Registered People", registered_people)
m2.metric("Training Samples", total_images)
m3.metric("Model Status", model_status)
m4.metric("Recent Logs", len(recent_logs_df) if not recent_logs_df.empty else 0)

st.write("")

# ---------------- DASHBOARD ----------------

if nav == "Dashboard":
    left, right = st.columns([1.08, 0.92], gap="large")

    with left:
        with st.container(border=True):
            st.markdown('<div class="section-title">Overview</div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="section-subtitle">A clean workflow summary with a premium glass panel.</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="feature-card">
                <div class="tiny-label">Workflow</div>
                <b>1.</b> Enroll a person with a clear face image.<br>
                <b>2.</b> Train the model after enough samples.<br>
                <b>3.</b> Recognize faces from camera or upload.<br>
                <b>4.</b> Review logs for attendance history.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            if dataset_df.empty:
                st.info("No enrolled users yet.")
            else:
                st.markdown('<div class="section-title">Enrolled People</div>', unsafe_allow_html=True)
                st.dataframe(dataset_df, width="stretch")

    with right:
        with st.container(border=True):
            st.markdown('<div class="section-title">Recent Activity</div>', unsafe_allow_html=True)
            st.markdown(
                '<div class="section-subtitle">Latest recognition entries appear here.</div>',
                unsafe_allow_html=True
            )

            if recent_logs_df.empty:
                st.info("No recognition logs available yet.")
            else:
                st.dataframe(recent_logs_df, width="stretch")

# ---------------- ENROLL ----------------

elif nav == "Enroll":
    st.markdown('<div class="section-title">Enroll a New Face</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Capture a face and save multiple augmented samples for better model quality.</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([0.96, 1.04], gap="large")

    with left:
        with st.container(border=True):
            person_name = st.text_input("Enter person name")

            input_method = st.radio(
                "Choose input method",
                ["Upload Image", "Use Camera"]
            )

            if input_method == "Upload Image":
                image_file = st.file_uploader(
                    "Upload face image",
                    type=["jpg", "jpeg", "png"]
                )
            else:
                image_file = st.camera_input("Capture face image")

            if st.button("Save Face Samples"):
                if image_file is None:
                    st.warning("Please upload or capture an image.")
                else:
                    image = Image.open(image_file)
                    success, message = save_face_image(person_name, pil_to_cv2(image))

                    if success:
                        st.success(message)
                    else:
                        st.error(message)

    with right:
        with st.container(border=True):
            st.markdown('<div class="section-title">Enrolled Dataset</div>', unsafe_allow_html=True)

            dataset_df = get_dataset_summary()

            if dataset_df.empty:
                st.info("No faces enrolled yet.")
            else:
                st.dataframe(dataset_df, width="stretch")

            st.markdown(
                """
                <div class="feature-card">
                <div class="tiny-label">Pro Tip</div>
                Use 5 to 10 images per person with different angles and lighting.
                This improves recognition accuracy and makes the model more resilient.
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- TRAIN ----------------

elif nav == "Train":
    st.markdown('<div class="section-title">Train Recognition Model</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Turn your enrolled dataset into a working LBPH recognition model.</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([0.82, 1.18], gap="large")

    with left:
        with st.container(border=True):
            st.write("Train the LBPH face recognition model using enrolled samples.")

            if st.button("Train Model"):
                success, message = train_model()

                if success:
                    st.success(message)
                else:
                    st.warning(message)

    with right:
        with st.container(border=True):
            st.markdown('<div class="section-title">Training Info</div>', unsafe_allow_html=True)

            st.markdown(
                """
                <div class="feature-card">
                <div class="tiny-label">How it works</div>
                Haar Cascade detects faces, converts them to grayscale, and LBPH learns the patterns.
                The trained model is saved inside the <b>trained_model</b> folder.
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- RECOGNIZE ----------------

elif nav == "Recognize":
    st.markdown('<div class="section-title">Recognize Faces</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Upload or capture an image and view recognition results with glowing overlays.</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([0.96, 1.04], gap="large")

    with left:
        with st.container(border=True):
            recognition_method = st.radio(
                "Choose recognition input",
                ["Upload Image", "Use Camera"]
            )

            if recognition_method == "Upload Image":
                recognition_file = st.file_uploader(
                    "Upload image for recognition",
                    type=["jpg", "jpeg", "png"]
                )
            else:
                recognition_file = st.camera_input("Capture image for recognition")

            if st.button("Recognize Face"):
                if recognition_file is None:
                    st.warning("Please upload or capture an image.")
                else:
                    image = Image.open(recognition_file)
                    output, results = recognize_faces(pil_to_cv2(image), threshold)

                    if output is None:
                        st.error(results)
                    elif isinstance(results, str):
                        st.warning(results)
                        st.image(
                            cv2_to_pil(output),
                            caption="Processed Image",
                            width="stretch"
                        )
                    else:
                        st.session_state.recognized_image = output
                        st.session_state.recognition_results = results

    with right:
        with st.container(border=True):
            if st.session_state.recognized_image is not None:
                st.image(
                    cv2_to_pil(st.session_state.recognized_image),
                    caption="Recognition Result",
                    width="stretch"
                )

                st.write("Recognition Results")
                st.dataframe(
                    pd.DataFrame(st.session_state.recognition_results),
                    width="stretch"
                )
            else:
                st.info("Recognition output will appear here.")

# ---------------- LOGS ----------------

elif nav == "Logs":
    st.markdown('<div class="section-title">Recognition Logs</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">View and download all recognition history in one place.</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        if os.path.exists(LOG_PATH):
            logs_df = pd.read_csv(LOG_PATH)

            st.dataframe(logs_df, width="stretch")

            st.download_button(
                label="Download Logs",
                data=logs_df.to_csv(index=False).encode("utf-8"),
                file_name="face_recognition_logs.csv",
                mime="text/csv"
            )
        else:
            st.info("No recognition logs available yet.")

# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer-note">Built with Python • Streamlit • OpenCV • Haar Cascade • LBPH Face Recognition</div>',
    unsafe_allow_html=True
)