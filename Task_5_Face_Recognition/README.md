

\# 🧠 Task 5: FaceVision AI — Face Detection \& Recognition System



<div align="center">



!\[Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

!\[Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)

!\[OpenCV](https://img.shields.io/badge/OpenCV-Computer\_Vision-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)

!\[AI](https://img.shields.io/badge/AI-Face\_Recognition-00D4AA?style=for-the-badge)

!\[Status](https://img.shields.io/badge/Status-Completed-28A745?style=for-the-badge)



\*\*A futuristic face detection and recognition application built using Python, Streamlit, OpenCV, Haar Cascade, and LBPH Face Recognition.\*\*



</div>



\---



\## 📌 Project Overview



| Field | Details |

|---|---|

| 🏷️ Project Name | FaceVision AI |

| 🏢 Internship | CodSoft Artificial Intelligence Internship |

| 📁 Task | Task 5 — Face Detection and Recognition |

| 💻 Language | Python |

| 🎨 Frontend | Streamlit |

| 👁️ Face Detection | Haar Cascade Classifier |

| 🧠 Face Recognition | LBPH Face Recognizer |

| 📊 Output | Recognition Result + Attendance Log |



\---



\## 🎯 Objective



The objective of this project is to build an AI-based application that can detect and recognize faces from images or camera input.



The system allows users to:



\- Enroll a new face

\- Train a recognition model

\- Recognize known and unknown faces

\- Store recognition history

\- Download recognition logs



This project demonstrates the practical use of computer vision in identity recognition and attendance-style applications.



\---



\## 📖 Description



\*\*FaceVision AI\*\* is a face detection and recognition system developed using Python and OpenCV.



The application uses \*\*Haar Cascade Classifier\*\* for face detection and \*\*LBPH Face Recognizer\*\* for face recognition. Users can enroll face images through upload or camera capture. The system automatically creates augmented face samples to improve recognition quality.



After training, the model can recognize enrolled users and mark unregistered faces as \*\*Unknown\*\*. It also stores recognition details such as name, confidence score, date, and time in a CSV log file.



The frontend is built using \*\*Streamlit\*\* with a modern neon glassmorphism dashboard design.



\---



\## ✨ Features



| # | Feature | Description |

|---|---|---|

| 1 | 👁️ Face Detection | Detects faces from uploaded images or camera input |

| 2 | 🧠 Face Recognition | Recognizes enrolled users using LBPH recognizer |

| 3 | 📌 Face Enrollment | Allows new users to enroll their face |

| 4 | 🔁 Data Augmentation | Creates multiple face samples from one image |

| 5 | 🏋️ Model Training | Trains the LBPH model using enrolled face samples |

| 6 | ❓ Unknown Handling | Marks unregistered faces as Unknown |

| 7 | 📊 Confidence Score | Displays recognition confidence score |

| 8 | 📝 Attendance Log | Saves recognition history with date and time |

| 9 | 📥 Log Download | Allows recognition logs to be downloaded as CSV |

| 10 | 🎨 Streamlit Dashboard | Modern sidebar-based neon UI |



\---



\## 🛠️ Technologies Used



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



\---



\## 🧠 AI / Computer Vision Techniques Used



\### 1. Haar Cascade Face Detection



Haar Cascade is used to locate human faces in an image. It detects face regions and returns bounding box coordinates.



In this project, Haar Cascade is used to:



```text

Detect faces

Crop face regions

Prepare training samples

Draw face bounding boxes

```



\---



\### 2. LBPH Face Recognition



LBPH stands for \*\*Local Binary Patterns Histograms\*\*.



It is used for recognizing faces by extracting texture-based facial patterns from grayscale face images.



In this project, LBPH is used to:



```text

Train on enrolled face samples

Predict the identity of a detected face

Return a confidence/distance score

Classify faces as known or unknown

```



\---



\### 3. Data Augmentation



To improve recognition, each enrolled face image is converted into multiple training samples:



```text

Original face

Flipped face

Brighter version

Darker version

Higher contrast version

Histogram equalized version

```



This helps the model handle small changes in lighting, expression, and camera conditions.



\---



\## ⚙️ How It Works



```text

User Enrolls Face

&#x20;       ↓

Face is Detected using Haar Cascade

&#x20;       ↓

Face Region is Cropped and Converted to Grayscale

&#x20;       ↓

Multiple Augmented Samples are Generated

&#x20;       ↓

LBPH Model is Trained

&#x20;       ↓

User Uploads/Captures Image for Recognition

&#x20;       ↓

Face is Detected Again

&#x20;       ↓

LBPH Predicts Identity

&#x20;       ↓

Known Face / Unknown Face is Displayed

&#x20;       ↓

Recognition Log is Saved

```



\---



\## 📂 Project Structure



```text

Task\_5\_Face\_Recognition/

│

├── app.py                  # Main Streamlit application

├── requirements.txt        # Required Python libraries

├── README.md               # Project documentation

├── .gitignore              # Prevents private data upload

│

├── dataset/                # Enrolled face samples

│   └── .gitkeep

│

├── trained\_model/          # Trained LBPH model and labels

│   └── .gitkeep

│

└── attendance\_logs/        # Recognition log CSV files

&#x20;   └── .gitkeep

```



\---



\## 📊 Dataset Information



The dataset is created by the user through face enrollment.



Each enrolled person gets a separate folder inside the `dataset` directory.



Example:



```text

dataset/

│

├── Rakshitha/

│   ├── Rakshitha\_001.jpg

│   ├── Rakshitha\_002.jpg

│   └── ...

│

└── Person\_2/

&#x20;   ├── Person\_2\_001.jpg

&#x20;   ├── Person\_2\_002.jpg

&#x20;   └── ...

```



For privacy reasons, the dataset is not uploaded to GitHub.



\---



\## 🚀 How to Run



\### Step 1: Install required libraries



```bash

pip install -r requirements.txt

```



\### Step 2: Run the Streamlit app



```bash

python -m streamlit run app.py

```



\---



\## 📦 Requirements



The `requirements.txt` file should contain:



```text

streamlit

opencv-contrib-python

numpy

pillow

pandas

```



\---



\## 🧪 How to Use the Application



\### 1. Enroll Face



```text

Go to Enroll

Enter person name

Upload or capture face image

Click Save Face Samples

```



\### 2. Train Model



```text

Go to Train

Click Train Model

Wait until model training completes

```



\### 3. Recognize Face



```text

Go to Recognize

Upload or capture an image

Adjust recognition threshold if needed

Click Recognize Face

```



\### 4. View Logs



```text

Go to Logs

View recognition history

Download CSV log file

```



\---



\## ✅ Recommended Enrollment Process



For better accuracy, enroll at least \*\*5 to 10 images per person\*\*.



Use different conditions:



```text

Normal face

Smiling face

Slight left angle

Slight right angle

Different lighting

Different distance from camera

Clear front-facing image

```



After adding new images, always click \*\*Train Model\*\* again.



\---



\## 📌 Recognition Threshold



The recognition threshold controls how strict the model is.



```text

Lower threshold = stricter recognition

Higher threshold = less strict recognition

```



Recommended threshold:



```text

90 to 105

```



If your face is detected as Unknown, increase the threshold slightly.



If the system misidentifies people, reduce the threshold.



\---



\## 📤 Output



The system displays:



```text

Detected face with bounding box

Recognized name

Confidence score

Unknown face label if not recognized

Recognition result table

Attendance / recognition log

```



\---



\## 📝 Recognition Log



Each successful recognition is saved in:



```text

attendance\_logs/recognition\_log.csv

```



The log contains:



| Column     | Description                  |

| ---------- | ---------------------------- |

| Name       | Recognized person name       |

| Confidence | Recognition confidence score |

| Date       | Recognition date             |

| Time       | Recognition time             |



\---



\## 🎨 UI Highlights



The application includes:



```text

Neon glassmorphism dashboard

Sidebar navigation

Quick statistics panel

Face enrollment section

Model training panel

Recognition workspace

Recent activity logs

Downloadable CSV logs

```



\---

\---



\## ⚠️ Limitations



```text

Recognition accuracy depends on lighting and image quality.

The system works best with clear front-facing faces.

LBPH is not as powerful as modern deep learning models like ArcFace or FaceNet.

The model should be retrained after adding new face samples.

This project is for educational and demonstration purposes.

```



\---



\## 🔮 Future Improvements



```text

Add real-time webcam video recognition

Use deep learning-based face detection

Add FaceNet or ArcFace for stronger recognition

Add login authentication

Add database support

Add admin dashboard

Add face spoof detection

Add exportable attendance reports

Add cloud deployment

```



\---



\## 🔐 Privacy Note



Face images are sensitive data.



For privacy protection, the following folders are excluded from GitHub:



```text

dataset/

trained\_model/

attendance\_logs/

```



Only empty folder placeholders are pushed using `.gitkeep`.



\---



\## 🏁 Conclusion



\*\*FaceVision AI\*\* is a practical face detection and recognition system that combines computer vision, machine learning, and an interactive Streamlit dashboard.



It demonstrates how faces can be enrolled, trained, recognized, and logged using OpenCV-based techniques.



This project helped me understand face detection, face recognition, dataset creation, model training, confidence thresholding, and real-world AI application design.



\---



<div align="center">



Made with ❤️ by \*\*Rakshitha R\*\*

CodSoft Artificial Intelligence Internship



</div>

```



