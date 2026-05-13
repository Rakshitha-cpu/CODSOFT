# 🤖 Task 1: Smart Student Assistant Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rule-Based AI](https://img.shields.io/badge/AI-Rule--Based-FF6F61?style=for-the-badge&logo=openai&logoColor=white)
![CodSoft](https://img.shields.io/badge/Internship-CodSoft-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-28a745?style=for-the-badge)

**A Python-based rule-driven chatbot built as part of the CodSoft AI Internship**

</div>

---

## 📌 Project Overview

| Field | Details |
|---|---|
| 🏷️ Project Name | Smart Student Assistant Chatbot |
| 🏢 Internship | CodSoft Artificial Intelligence Internship |
| 📁 Task | Task 1 — Chatbot with Rule-Based Responses |
| 💻 Language | Python |
| 🧠 Approach | If-Else Logic + Keyword Matching |

---

## 🎯 Objective

> Build a simple chatbot that responds to user inputs using **predefined rules** — no machine learning, no external AI APIs. Just clean Python logic.

The chatbot uses **if-else statements** and **keyword matching** to identify user intent and return appropriate responses — simulating a basic conversational assistant for students.

---

## 📖 Description

This is a **rule-based chatbot** developed purely in Python. Here's how it works under the hood:

- 📥 Takes user input from the terminal
- 🔡 Converts it to **lowercase** for uniform matching
- 🔍 Scans for **keywords** using conditional logic
- 💬 Returns a **predefined response** based on the matched keyword
- 🔁 Loops until the user says `bye`, `exit`, or `quit`

Through this project, I got hands-on experience with **text preprocessing**, **conversation flow design**, and the fundamentals of **Natural Language Processing (NLP)**.

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1 | 👋 Greeting | Responds to hello, hi, hey |
| 2 | 🙋 Name Query | Tells the user its name |
| 3 | 📚 Study Tips | Shares helpful student study strategies |
| 4 | 💼 Internship Guidance | Gives tips on finding and applying for internships |
| 5 | 🐍 Python Help | Explains Python basics |
| 6 | 🤖 AI Info | Describes what Artificial Intelligence is |
| 7 | 🐙 GitHub Guide | Explains how to use GitHub |
| 8 | 🔗 LinkedIn Guide | Tips on building a LinkedIn profile |
| 9 | ⏰ Current Time | Fetches and displays real-time clock |
| 10 | 📅 Current Date | Fetches and displays today's date |
| 11 | 😄 Jokes | Tells a random joke to lighten the mood |
| 12 | 💪 Motivation | Shares an inspirational quote |
| 13 | 🕘 Chat History | Stores and displays full conversation history |
| 14 | 👋 Exit | Graceful goodbye on `bye`, `exit`, `quit` |
| 15 | ❓ Fallback | Smart default reply for unrecognized inputs |

---

## 🛠️ Technologies Used

```
✅ Python 3.x
✅ if-else conditional logic
✅ Keyword / pattern matching
✅ Lists & Functions
✅ random  module
✅ datetime module
```

---

## ⚙️ How It Works

```
User Input
    │
    ▼
Convert to Lowercase
    │
    ▼
Check Keywords using if-else
    │
    ├── Keyword Found? ──► Return Matched Response
    │
    └── No Match?      ──► Return Fallback Response
    │
    ▼
Continue Loop (until bye / exit / quit)
```

---

## 🚀 How to Run

**Step 1 — Navigate to project folder:**
```bash
cd Task_1_Chatbot
```

**Step 2 — Run the chatbot:**
```bash
python chatbot.py
```

---

## 💬 Sample Inputs to Try

```text
hello
help
what is your name
give me study tips
tell me about internship
what is python
what is ai
github
linkedin
tell me a joke
give motivation
what is the time
what is the date
show history
bye
```

---

## 📂 Project Structure

```
Task_1_Chatbot/
│
├── chatbot.py       ← Main chatbot logic
└── README.md        ← Project documentation (you are here!)
```

---

## 📚 What I Learned

- ✅ How rule-based chatbots work using keyword matching
- ✅ Text preprocessing with lowercase conversion
- ✅ Designing multi-branch conversational logic using if-else
- ✅ Using `datetime` and `random` modules in real applications
- ✅ Maintaining and displaying chat history using lists
- ✅ Understanding the foundations of NLP before jumping into ML

---

## 🏁 Conclusion

This **Smart Student Assistant Chatbot** is a beginner-friendly, rule-based project that demonstrates how conversation logic can be structured purely using Python. It forms a solid foundation for understanding how more advanced AI chatbots work.

---

<div align="center">

Made with ❤️ by **Rakshitha R** | CodSoft AI Internship

</div>
