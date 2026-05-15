\# 💼 Task 4: Smart Job Recommendation System



<div align="center">



!\[Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

!\[Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)

!\[Machine Learning](https://img.shields.io/badge/ML-Recommendation\_System-7C3AED?style=for-the-badge)

!\[Status](https://img.shields.io/badge/Status-Completed-28A745?style=for-the-badge)



\*\*A job recommendation system that suggests suitable job roles based on candidate skills, location, experience level, and job similarity.\*\*



</div>



\---



\## 📌 Project Overview



| Field | Details |

|---|---|

| 🏷️ Project Name | Smart Job Recommendation System |

| 🏢 Internship | CodSoft Artificial Intelligence Internship |

| 📁 Task | Task 4 — Recommendation System |

| 💻 Language | Python |

| 🎨 Frontend | Streamlit |

| 🧠 Approach | Content-Based Filtering |

| ⚙️ Algorithm | TF-IDF Vectorization + Cosine Similarity |



\---



\## 🎯 Objective



The objective of this project is to build a recommendation system that suggests suitable job roles to users based on their preferences and skills.



This system recommends jobs by comparing candidate skills with job requirements using \*\*content-based filtering\*\*.



\---



\## 📖 Description



The \*\*Smart Job Recommendation System\*\* is an HR-tech style recommendation application built using Python and Streamlit.



The user can enter their skills or select a preferred job role. The system then analyzes the available job dataset and recommends the most relevant job roles based on similarity.



The project uses \*\*TF-IDF Vectorization\*\* to convert job-related text data into numerical vectors and \*\*Cosine Similarity\*\* to calculate how closely a job matches the user profile.



\---



\## ✨ Features



| # | Feature | Description |

|---|---|---|

| 1 | 💼 Job Recommendation | Recommends suitable jobs based on user input |

| 2 | 🧠 Skill-Based Search | User can enter skills to find matching jobs |

| 3 | 🎯 Role-Based Search | User can select a job role and find similar roles |

| 4 | 📍 Location Filter | Filters jobs based on preferred location |

| 5 | ⚡ Experience Filter | Filters jobs based on experience level |

| 6 | 📊 Match Score | Shows similarity percentage for each job |

| 7 | ✅ Matched Skills | Displays skills already matching the job |

| 8 | 📌 Missing Skills | Shows skills the candidate needs to improve |

| 9 | 📁 Dataset Driven | Uses a structured jobs.csv dataset |

| 10 | 🎨 Streamlit UI | Clean, colorful, interactive frontend |



\---



\## 🛠️ Technologies Used



```text

Python

Streamlit

Pandas

Scikit-learn

TF-IDF Vectorizer

Cosine Similarity

Content-Based Filtering





🧠 Recommendation Technique Used

Content-Based Filtering



Content-based filtering recommends items by comparing item features.



In this project, jobs are recommended based on:



Job Title

Required Skills

Experience Level

Location

Job Description



The system compares these features with the user's skills or selected job role.



⚙️ How It Works

User Input

&#x20;   ↓

Skills / Job Role Selection

&#x20;   ↓

Job Dataset Loaded

&#x20;   ↓

Text Features Combined

&#x20;   ↓

TF-IDF Vectorization

&#x20;   ↓

Cosine Similarity Calculation

&#x20;   ↓

Top Matching Jobs Recommended

&#x20;   ↓

Skill Gap Analysis Displayed

🧮 Algorithm Explanation

1\. TF-IDF Vectorization



TF-IDF converts text data into numerical form by identifying important words in the dataset.



For example:



Python SQL Machine Learning



is converted into a numerical vector that the system can compare with job descriptions.



2\. Cosine Similarity



Cosine similarity measures how similar two vectors are.



A higher score means the candidate profile and job role are more similar.



Higher similarity score = Better job match

📂 Project Structure

Task\_4\_Recommendation\_System/

│

├── app.py              # Streamlit frontend

├── recommender.py      # Recommendation logic

├── jobs.csv            # Job dataset

├── requirements.txt    # Required libraries

└── README.md           # Project documentation

📊 Dataset Description



The dataset contains job-related information such as:



Column	Description

job\_id	Unique job ID

job\_title	Name of the job role

company	Company name

location	Job location

experience\_level	Entry Level or Mid Level

skills	Required skills for the job

description	Job role description

🚀 How to Run

Step 1: Install required libraries

pip install -r requirements.txt

Step 2: Run the Streamlit app

python -m streamlit run app.py

🧪 Sample Inputs to Try

Python SQL Machine Learning

HTML CSS JavaScript React

PowerBI Excel SQL

Docker Kubernetes AWS Linux

✅ Sample Output



For input:



Python SQL Machine Learning



The system may recommend jobs such as:



Machine Learning Engineer

Data Scientist

AI Engineer

Data Analyst

Data Engineer



Each result includes:



Match Score

Company Name

Location

Experience Level

Required Skills

Matched Skills

Missing Skills

📌 Key Learning Outcomes



Through this project, I learned:



✅ How recommendation systems work

✅ How content-based filtering is implemented

✅ How TF-IDF converts text into vectors

✅ How cosine similarity finds matching items

✅ How to build an interactive ML app using Streamlit

✅ How to perform skill gap analysis

✅ How recommendation systems are used in HR-tech platforms







⚠️ Limitations

The dataset is small and manually created for demonstration.

The system does not use real-time job portal data.

Recommendation quality depends on the quality of job descriptions and skill keywords.

🔮 Future Improvements

Add larger real-world job dataset

Add resume upload and resume parsing

Add user authentication

Add company-wise job filtering

Add salary-based filtering

Add collaborative filtering

Add real-time job API integration

🏁 Conclusion



The Smart Job Recommendation System demonstrates how recommendation systems can be used in HR-tech applications.



It combines content-based filtering, TF-IDF vectorization, cosine similarity, and skill gap analysis to recommend suitable job roles to candidates.



This project helped me understand how recommendation engines work in real-world platforms such as job portals and career recommendation systems.



<div align="center">



Made with ❤️ by Rakshitha R

CodSoft Artificial Intelligence Internship



</div> ```





