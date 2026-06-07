<div align="center">

```
 ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗
 ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║
 ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║
 ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║
  ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║
   ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        C A P T I O N   A I
```

# 🖼️ VisionCaption AI — Image Captioning with BLIP

> **CodSoft Artificial Intelligence Internship | Task 3**
> A smart image captioning system powered by Vision-Language Transformers

<br/>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-BLIP-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-Model-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

---

## 📌 Project Overview

**VisionCaption AI** is an intelligent image captioning application built as part of the **CodSoft AI Internship**. It bridges **Computer Vision** and **Natural Language Processing** by using a pre-trained **BLIP transformer model** to automatically generate natural language descriptions for any uploaded image.

The system goes beyond automation — it includes a **human review layer**, allowing users to select, edit, and download the best caption output.

```
  📷 Upload Image  ──►  🧠 BLIP Model  ──►  ✍️ Review & Edit  ──►  💾 Save / Download
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📤 Image Upload | Supports **JPG, JPEG, PNG** formats |
| 🖼️ Image Preview | View uploaded image before processing |
| 🤖 Auto Captions | Generate multiple caption suggestions |
| 🧠 BLIP Model | Pre-trained transformer for vision-language understanding |
| 📝 Editable Caption | Manually refine the AI-generated output |
| 📖 Detailed Caption | Generate a rich, descriptive caption |
| 📱 Social Media Caption | Generate short, engaging captions |
| 💾 Download | Export final captions as text files |
| 📚 Caption History | Save and revisit previous captions |
| 📐 Image Metadata | Display width, height, and file format |
| 🎨 Clean UI | Simple and responsive Streamlit frontend |

---

## 🧠 The BLIP Model

This project uses the **Salesforce BLIP Image Captioning** model — a state-of-the-art vision-language transformer:

```
Model: Salesforce/blip-image-captioning-base
Source: Hugging Face Transformers Hub
Type: Vision-Language Pre-training (BLIP)
Task: Image-to-Text Caption Generation
```

### What is BLIP?

**BLIP** (Bootstrapped Language-Image Pre-training) is a transformer-based model that jointly learns visual and language representations. It can "look" at an image and generate fluent, natural language descriptions by connecting visual features to language context.

```
 ┌──────────────────────────────────────────────────────────┐
 │                     BLIP Architecture                    │
 │                                                          │
 │   🖼️ Image  ──►  Vision Encoder  ──►  Image Features    │
 │                        │                    │            │
 │                        └──────┬─────────────┘            │
 │                               ▼                          │
 │                    Cross-Attention Module                 │
 │                               │                          │
 │   📝 Text  ◄──  Language Decoder  ◄──  Fused Features   │
 └──────────────────────────────────────────────────────────┘
```

### Why Use a Pre-Trained Model?

Training an image captioning model from scratch demands:

- 🗄️ Millions of image-caption pairs
- ⏳ Weeks of training time
- 🖥️ High-end GPU clusters

Using **Salesforce/blip-image-captioning-base** gives us state-of-the-art performance **instantly** — without any training overhead.

---

## 🔄 How It Works

```
        ┌──────────────────────────────────┐
        │         User Uploads Image        │
        │      (JPG / JPEG / PNG)           │
        └──────────────┬───────────────────┘
                       │
        ┌──────────────▼───────────────────┐
        │        Image Preprocessing        │
        │   Resize · Normalize · Tokenize   │
        └──────────────┬───────────────────┘
                       │
        ┌──────────────▼───────────────────┐
        │    BLIP Model Analyzes Image      │
        │  Vision Encoder + Language Model  │
        └──────────────┬───────────────────┘
                       │
        ┌──────────────▼───────────────────┐
        │     Caption Suggestions Generated │
        │  Standard · Detailed · Social     │
        └──────────────┬───────────────────┘
                       │
        ┌──────────────▼───────────────────┐
        │     Human Review & Editing        │
        │   Select best · Edit manually     │
        └──────────────┬───────────────────┘
                       │
        ┌──────────────▼───────────────────┐
        │    Download or Save to History    │
        └──────────────────────────────────┘
```

---

## 🗂️ Project Structure

```
Task_3_Image_Captioning/
│
├── 📄 app.py                  # Streamlit frontend & UI logic
├── 📄 image_captioning.py     # BLIP model loading & inference
├── 📄 requirements.txt        # Python dependencies
└── 📄 README.md               # Project documentation
```

---

## ⚙️ Technologies Used

```
┌──────────────────────────────────────────────────────────┐
│  🐍  Python          Core programming language           │
│  🌐  Streamlit       Interactive web frontend            │
│  🖼️  Pillow          Image loading and preprocessing     │
│  🤗  Transformers    BLIP model loading via HuggingFace  │
│  🔥  PyTorch         Deep learning inference backend     │
│  🧠  BLIP Model      Vision-language caption generation  │
└──────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/visioncaption-ai.git
cd visioncaption-ai/Task_3_Image_Captioning

# 2. Install all dependencies
pip install -r requirements.txt
```

### Run the App

```bash
# Launch the Streamlit frontend
python -m streamlit run app.py
```

> The app will open automatically at `http://localhost:8501`

---

## 📦 Requirements

```txt
streamlit
Pillow
transformers
torch
torchvision
```

---

## 🎯 Caption Types

### 📝 Standard Caption
> A concise, factual description of the image content.
```
"a dog running on a green grass field"
```

### 📖 Detailed Caption
> A richer, more descriptive paragraph with context and details.
```
"a golden retriever running joyfully across a sunlit green grass
 field, with trees visible in the background on a clear afternoon"
```

### 📱 Social Media Caption
> A short, catchy caption suitable for Instagram or Twitter.
```
"Living for the outdoors 🐾🌿 #DogsOfInstagram #NatureLovers"
```

---

## ⚠️ Limitations

The BLIP model may generate less accurate captions when:

```
  ❌  Image is dark or low resolution
  ❌  Objects are very small in the frame
  ❌  Hand gestures are the main subject
  ❌  Background details are visually complex
  ❌  Abstract or artistic images with no clear subject
```

> **Solution:** The project includes a **human review and editable caption feature** — users can always correct or refine the AI output before saving.

---

## 💡 What I Learned

Through building VisionCaption AI, I gained hands-on experience in:

```
  ✅  How Computer Vision and NLP work together
  ✅  How to load and use pre-trained transformer models
  ✅  How image captioning pipelines are structured
  ✅  How to build a practical AI app with Streamlit
  ✅  How to handle model limitations with human-in-the-loop design
  ✅  How to create a complete, end-to-end AI workflow
```

---

## 🏁 Conclusion

**VisionCaption AI** demonstrates the power of pre-trained vision-language models in building real-world applications. By combining the **BLIP transformer model** with a clean **Streamlit interface** and a **human review layer**, the project delivers a practical, usable, and intelligent image captioning tool — with minimal infrastructure required.

---

## 👤 Author

**Internship:** CodSoft Artificial Intelligence Internship
**Task:** Task 3 — Image Captioning AI
**Stack:** Python · Streamlit · HuggingFace Transformers · BLIP · PyTorch

---

## 📄 License

This project is created for educational and internship purposes under **CodSoft**.

---

<div align="center">

*Built with ❤️ and the power of Vision-Language Transformers*

*"A picture is worth a thousand words — AI picks the best ones."*

</div>
