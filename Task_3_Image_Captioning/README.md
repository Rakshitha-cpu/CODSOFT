\# Task 3: Image Captioning AI



\## Project Title

VisionCaption AI



\## Internship

CodSoft Artificial Intelligence Internship



\## Objective

The objective of this project is to build an Image Captioning AI system that combines Computer Vision and Natural Language Processing to generate captions for uploaded images.



\## Description

VisionCaption AI is an image captioning application built using Python and Streamlit. The user uploads an image, and the system generates natural language caption suggestions using a pre-trained BLIP transformer-based image captioning model.



The project also includes human review, where users can select the best caption suggestion and edit the final caption before downloading it.



\## Features

\- Upload JPG, JPEG, or PNG images

\- Preview uploaded image

\- Generate image caption suggestions

\- Use a pre-trained BLIP transformer model

\- Edit final caption manually

\- Generate detailed caption

\- Generate social media caption

\- Download generated captions

\- Save captions to history

\- Display image width, height, and format

\- Clean Streamlit frontend



\## Technologies Used

\- Python

\- Streamlit

\- Pillow

\- Transformers

\- PyTorch

\- BLIP Image Captioning Model



\## Model Used

This project uses the pre-trained BLIP image captioning model:



```text

Salesforce/blip-image-captioning-base



BLIP is a transformer-based vision-language model that can understand image features and generate natural language descriptions.



How It Works

Upload Image

&#x20;   ↓

Image Preprocessing

&#x20;   ↓

BLIP Model Analyzes Image

&#x20;   ↓

Caption Suggestions Generated

&#x20;   ↓

User Reviews and Edits Caption

&#x20;   ↓

Final Caption Downloaded or Saved





Why Pre-Trained Model is Used



Training an image captioning model from scratch requires a very large image-caption dataset and high computational power. Therefore, this project uses a pre-trained BLIP model to generate captions efficiently.



How to Run

Step 1: Install requirements

pip install -r requirements.txt

Step 2: Run the app

python -m streamlit run app.py

Project Structure

Task\_3\_Image\_Captioning/

│

├── app.py

├── image\_captioning.py

├── requirements.txt

└── README.md

Limitations



Image captioning models may sometimes generate inaccurate captions, especially when:



The image is dark or unclear

Objects are small

Hand gestures are present

Background details are confusing



To handle this, the project includes a human review and editable final caption feature.



What I Learned



Through this project, I learned:



How computer vision and NLP work together

How to use pre-trained transformer models

How image captioning works

How to build an AI app using Streamlit

How to handle model limitations with human review

How to create a practical AI workflow





Conclusion



VisionCaption AI demonstrates how a pre-trained transformer-based model can generate captions for images. The project combines image understanding and natural language generation in a simple and practical AI application.



