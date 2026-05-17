

````markdown
# 🧠 Task 5: FaceVision AI — Face Detection & Recognition System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![AI](https://img.shields.io/badge/AI-Face%20Recognition-00D4AA?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-28A745?style=for-the-badge)

**A futuristic face detection and recognition system built using Python, Streamlit, OpenCV, Haar Cascade, and LBPH Face Recognition.**

</div>

---

## 📌 Project Overview

**FaceVision AI** is an AI-powered computer vision application that detects and recognizes faces from uploaded images or camera input.

The system allows users to enroll faces, train a face recognition model, recognize known users, identify unknown faces, and store recognition logs.

This project was developed as part of the **CodSoft Artificial Intelligence Internship**.

---

## 🏢 Internship Details

| Field | Details |
|---|---|
| Internship | CodSoft Artificial Intelligence Internship |
| Task | Task 5 — Face Detection and Recognition |
| Project Name | FaceVision AI |
| Domain | Computer Vision |
| Language | Python |
| Frontend | Streamlit |
| Face Detection | Haar Cascade Classifier |
| Face Recognition | LBPH Face Recognizer |
| Log Storage | CSV File |

---

## 🎯 Objective

The objective of this project is to develop an AI application that can detect and recognize faces in images or camera input.

The system demonstrates how computer vision can be used for identity recognition, attendance tracking, and access-control style applications.

---

## 📖 Project Description

FaceVision AI is a face detection and recognition system built with **Python**, **Streamlit**, and **OpenCV**.

The application uses **Haar Cascade Classifier** for face detection and **LBPH Face Recognizer** for face recognition.

Users can enroll faces through image upload or camera input. The system detects the face, crops the face region, converts it into grayscale, and saves multiple augmented samples for better recognition performance.

After training, the model can recognize enrolled users and mark unregistered faces as **Unknown**. Recognition details such as name, confidence score, date, and time are stored in a CSV log file.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| Face Detection | Detects faces from uploaded images or camera input |
| Face Enrollment | Allows users to register new faces |
| Face Recognition | Recognizes enrolled users using LBPH model |
| Unknown Face Handling | Marks unregistered faces as Unknown |
| Data Augmentation | Generates multiple training samples from one image |
| Model Training | Trains the LBPH recognizer using enrolled samples |
| Confidence Score | Displays recognition confidence information |
| Recognition Logs | Saves recognized user details with date and time |
| Download Logs | Allows recognition logs to be downloaded as CSV |
| Streamlit Dashboard | Provides a modern neon glassmorphism interface |

---

## 🛠️ Technologies Used

```text
Python
Streamlit
OpenCV
NumPy
Pillow
Pandas
Haar Cascade Classifier
LBPH Face Recognizer
````

---

## 🧠 Algorithms and Techniques Used

### 1. Haar Cascade Classifier

Haar Cascade is used for face detection. It scans the image and detects face regions using trained facial features.

In this project, Haar Cascade is used to:

```text
Detect face regions
Crop detected faces
Draw bounding boxes around faces
Prepare face samples for training
```

---

### 2. LBPH Face Recognizer

LBPH stands for **Local Binary Patterns Histograms**.

It is used for face recognition by analyzing texture-based patterns from grayscale face images.

In this project, LBPH is used to:

```text
Train the face recognition model
Predict the identity of detected faces
Generate recognition confidence values
Classify faces as known or unknown
```

---

### 3. Data Augmentation

To improve recognition accuracy, the system generates multiple training samples from one enrolled face image.

For each detected face, the system creates:

```text
Original face sample
Flipped face sample
Brighter face sample
Darker face sample
High contrast face sample
Histogram equalized face sample
```

This helps the model perform better under small changes in lighting, expression, and camera conditions.

---

## ⚙️ System Workflow

```text
User Enrolls Face
        ↓
Face Detection using Haar Cascade
        ↓
Face Cropping and Grayscale Conversion
        ↓
Augmented Face Samples Generated
        ↓
LBPH Model Training
        ↓
Image or Camera Input for Recognition
        ↓
Face Detection
        ↓
Face Recognition Prediction
        ↓
Known / Unknown Result Displayed
        ↓
Recognition Log Saved
```

---

## 📂 Project Structure

```text
Task_5_Face_Recognition/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── .gitkeep
│
├── trained_model/
│   └── .gitkeep
│
└── attendance_logs/
    └── .gitkeep
```

---

## 📁 Folder Explanation

| Folder / File    | Description                                             |
| ---------------- | ------------------------------------------------------- |
| app.py           | Main Streamlit application                              |
| requirements.txt | Required Python packages                                |
| README.md        | Project documentation                                   |
| dataset/         | Stores enrolled face samples                            |
| trained_model/   | Stores trained LBPH model and label data                |
| attendance_logs/ | Stores recognition log CSV files                        |
| .gitignore       | Prevents private face data and logs from being uploaded |

---

## 📦 Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
streamlit
opencv-contrib-python
numpy
pillow
pandas
```

---

## 🚀 How to Run the Project

### Step 1: Open the project folder

```bash
cd Task_5_Face_Recognition
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit app

```bash
python -m streamlit run app.py
```

---

## 🧪 How to Use

### Step 1: Enroll Face

```text
Open the Enroll section
Enter the person name
Upload or capture a clear face image
Click Save Face Samples
```

### Step 2: Train Model

```text
Open the Train section
Click Train Model
Wait until training completes
```

### Step 3: Recognize Face

```text
Open the Recognize section
Upload or capture an image
Adjust threshold if needed
Click Recognize Face
```

### Step 4: View Logs

```text
Open the Logs section
View recognition history
Download logs as CSV
```

---

## ✅ Recommended Enrollment Practice

For better recognition accuracy, enroll multiple images for each person.

Recommended samples:

```text
Normal face
Smiling face
Slight left angle
Slight right angle
Different lighting condition
Different camera distance
Clear front-facing image
```

Minimum recommended images per person:

```text
5 to 10 images
```

After adding new face samples, the model must be trained again.

---

## 🎚️ Recognition Threshold

The recognition threshold controls how strict the model is.

```text
Lower threshold = stricter recognition
Higher threshold = less strict recognition
```

Recommended threshold range:

```text
90 to 105
```

If a known face is shown as Unknown, increase the threshold slightly.

If the system wrongly recognizes unknown people, reduce the threshold.

---

## 📊 Recognition Log

Each successful recognition is stored in:

```text
attendance_logs/recognition_log.csv
```

The log contains:

| Column     | Description                  |
| ---------- | ---------------------------- |
| Name       | Recognized person name       |
| Confidence | Recognition confidence score |
| Date       | Date of recognition          |
| Time       | Time of recognition          |

---

## 🔐 Privacy Note

Face images and trained models contain sensitive personal data.

For privacy protection, the following folders should not be uploaded with real data:

```text
dataset/
trained_model/
attendance_logs/
```

Only empty folder placeholders are kept using `.gitkeep`.

---

## ⚠️ Limitations

```text
Recognition accuracy depends on lighting and image quality.
The system works best with clear front-facing images.
LBPH is less powerful than modern deep learning models such as FaceNet or ArcFace.
The model must be retrained after adding new face samples.
Large changes in face angle or expression may reduce accuracy.
```

---

## 🔮 Future Improvements

```text
Add real-time webcam video recognition
Add deep learning-based face detection
Use FaceNet or ArcFace for stronger recognition
Add face spoof detection
Add database support
Add admin authentication
Add attendance report generation
Add cloud deployment
Improve recognition under low-light conditions
```

---

## 📚 Learning Outcomes

Through this project, I learned:

```text
How face detection works using Haar Cascade
How face recognition works using LBPH
How to collect and prepare face datasets
How to train and save a recognition model
How confidence thresholding works
How to handle unknown faces
How to build a Streamlit-based computer vision dashboard
How to store recognition logs using CSV files
```

---

## 🏁 Conclusion

FaceVision AI is a practical computer vision application that combines face detection, face recognition, model training, and recognition logging.

The system demonstrates how OpenCV-based techniques can be used to build an identity recognition system with an interactive Streamlit frontend.

This project helped me understand the complete workflow of a face recognition application, from enrollment and training to recognition and logging.

---

<div align="center">

Made with ❤️ by **Rakshitha R**
CodSoft Artificial Intelligence Internship

</div>
```

The badge links will look messy inside a plain text editor, but they will render properly on GitHub.
