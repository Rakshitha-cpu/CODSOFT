import streamlit as st
import datetime
import random
import html

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart Assistant Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- RULE-BASED DATA ----------------

greetings = ["hello", "hi", "hey", "good morning", "good evening"]
farewells = ["bye", "exit", "quit"]
name_questions = ["your name", "who are you", "what are you"]

study_keywords = ["study", "exam", "revision", "learn"]
internship_keywords = ["internship", "codsoft", "task"]
python_keywords = ["python", "programming", "coding"]
ai_keywords = ["ai", "artificial intelligence", "machine learning"]
github_keywords = ["github", "repository", "repo"]
linkedin_keywords = ["linkedin", "post", "profile"]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why was the Python developer calm? Because he handled exceptions."
]

quotes = [
    "Small daily progress is better than fake big plans.",
    "Do not just watch tutorials. Build projects.",
    "Consistency beats motivation."
]

# ---------------- BOT RESPONSE FUNCTION ----------------

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! What would you like to learn?",
            "Hey! I am ready to help you."
        ])

    elif any(word in user_input for word in farewells):
        return "Goodbye! Keep learning and building."

    elif "help" in user_input:
        return (
            "You can ask me about study tips, Python, artificial intelligence, "
            "internship guidance, GitHub, LinkedIn, time, date, jokes, and motivation."
        )

    elif any(word in user_input for word in name_questions):
        return "I am Smart Assistant, a rule-based chatbot built using Python."

    elif "how are you" in user_input:
        return "I am working perfectly and ready to help."

    elif any(word in user_input for word in study_keywords):
        return (
            "Study tip: Use focused study sessions, revise daily, and solve problems "
            "instead of only reading theory."
        )

    elif any(word in user_input for word in internship_keywords):
        return (
            "Internship tip: Build clean projects, write documentation, upload your code "
            "to GitHub, and prepare a clear demo video."
        )

    elif any(word in user_input for word in python_keywords):
        return (
            "Python is a beginner-friendly programming language used for automation, "
            "web development, data analysis, and artificial intelligence."
        )

    elif any(word in user_input for word in ai_keywords):
        return (
            "Artificial Intelligence is the field of making machines perform tasks that "
            "normally require human intelligence, such as learning and decision-making."
        )

    elif any(word in user_input for word in github_keywords):
        return (
            "GitHub tip: Keep your repository organized with folders, clean code, "
            "meaningful file names, and a proper README file."
        )

    elif any(word in user_input for word in linkedin_keywords):
        return (
            "LinkedIn tip: Share your project with a short demo, clear explanation, "
            "GitHub link, and relevant hashtags."
        )

    elif "time" in user_input:
        return "Current time is " + datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in user_input:
        return "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "motivation" in user_input or "quote" in user_input:
        return random.choice(quotes)

    else:
        return "I do not have a rule for that yet. Try typing help."

# ---------------- CSS DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 45%, #f093fb 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 920px;
    padding-top: 35px;
    padding-bottom: 35px;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main header */
.header {
    text-align: center;
    margin-bottom: 25px;
}

.logo {
    width: 78px;
    height: 78px;
    background: linear-gradient(135deg, #6366f1, #ec4899);
    border-radius: 24px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    margin-bottom: 14px;
    box-shadow: 0 12px 30px rgba(99, 102, 241, 0.35);
}

.title {
    font-size: 44px;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 6px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.25);
}

.subtitle {
    color: #f3f4f6;
    font-size: 17px;
    font-weight: 500;
}

/* Chips */
.chip-row {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 28px;
}

.chip {
    background: rgba(255,255,255,0.95);
    color: #374151;
    padding: 9px 15px;
    border-radius: 999px;
    font-weight: 800;
    font-size: 14px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}

/* Section title */
.section-title {
    color: white;
    font-size: 18px;
    font-weight: 900;
    margin-bottom: 12px;
    text-shadow: 0 3px 12px rgba(0,0,0,0.25);
}

/* Chat area */
.chat-area {
    background: linear-gradient(180deg, #ffffff, #f8fafc);
    border-radius: 28px;
    padding: 24px;
    height: 430px;
    overflow-y: auto;
    margin-top: 18px;
    margin-bottom: 22px;
    box-shadow: 0 25px 70px rgba(31, 38, 135, 0.32);
    border: 1px solid rgba(255,255,255,0.45);
}

/* Message rows */
.message-row {
    display: flex;
    margin-bottom: 16px;
}

.message-row.user {
    justify-content: flex-end;
}

.message-row.bot {
    justify-content: flex-start;
}

/* Message bubbles */
.bubble {
    max-width: 75%;
    padding: 14px 18px;
    border-radius: 20px;
    line-height: 1.55;
    font-size: 15px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.bot-bubble {
    background: #ffffff;
    color: #111827;
    border-bottom-left-radius: 6px;
    border: 1px solid #e5e7eb;
}

.user-bubble {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-bottom-right-radius: 6px;
}

.sender {
    font-size: 12px;
    font-weight: 900;
    margin-bottom: 5px;
    opacity: 0.8;
}

/* Input */
.stTextInput label {
    color: white !important;
    font-weight: 900 !important;
    font-size: 16px !important;
}

.stTextInput input {
    background: #ffffff !important;
    color: #111827 !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 16px !important;
    padding: 14px !important;
    font-size: 15px !important;
}

.stTextInput input:focus {
    border: 2px solid #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.20) !important;
}

.stTextInput input::placeholder {
    color: #9ca3af !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #ec4899) !important;
    color: white !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 12px 18px !important;
    font-weight: 900 !important;
    width: 100%;
    box-shadow: 0 10px 25px rgba(99,102,241,0.25);
}

.stButton > button:hover {
    transform: translateY(-2px);
    color: white !important;
    box-shadow: 0 14px 30px rgba(99,102,241,0.35);
}

.stDownloadButton > button {
    background: #111827 !important;
    color: white !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 12px 18px !important;
    font-weight: 900 !important;
    width: 100%;
}

/* Footer */
.footer {
    text-align: center;
    color: white;
    font-size: 13px;
    font-weight: 600;
    margin-top: 24px;
    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "sender": "bot",
            "text": "Hello! I am your Smart Assistant. Type help to see what I can do."
        }
    ]

# ---------------- HEADER ----------------

st.markdown("""
<div class="header">
    <div class="logo">🤖</div>
    <div class="title">Smart Assistant</div>
    <div class="subtitle">A colorful rule-based chatbot built with Python</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chip-row">
    <div class="chip">Rule-Based</div>
    <div class="chip">Keyword Matching</div>
    <div class="chip">Python Powered</div>
    <div class="chip">Chat History</div>
</div>
""", unsafe_allow_html=True)

# ---------------- QUICK QUESTIONS ----------------

st.markdown('<div class="section-title">Quick Questions</div>', unsafe_allow_html=True)

q1, q2, q3, q4 = st.columns(4)

quick_prompt = None

with q1:
    if st.button("Study Tips"):
        quick_prompt = "study tips"

with q2:
    if st.button("Python"):
        quick_prompt = "what is python"

with q3:
    if st.button("AI"):
        quick_prompt = "what is ai"

with q4:
    if st.button("Joke"):
        quick_prompt = "tell me a joke"

if quick_prompt:
    st.session_state.messages.append({"sender": "user", "text": quick_prompt})
    response = get_bot_response(quick_prompt)
    st.session_state.messages.append({"sender": "bot", "text": response})
    st.rerun()

# ---------------- CHAT DISPLAY ----------------
# Important: whole chat is rendered as one HTML block to avoid empty white box issue.

chat_html = '<div class="chat-area">'

for message in st.session_state.messages:
    safe_text = html.escape(message["text"]).replace("\n", "<br>")

    if message["sender"] == "user":
        chat_html += f"""
        <div class="message-row user">
            <div class="bubble user-bubble">
                <div class="sender">You</div>
                {safe_text}
            </div>
        </div>
        """
    else:
        chat_html += f"""
        <div class="message-row bot">
            <div class="bubble bot-bubble">
                <div class="sender">Assistant</div>
                {safe_text}
            </div>
        </div>
        """

chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)

# ---------------- INPUT FORM ----------------

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Message",
        placeholder="Type your message here..."
    )

    send_clicked = st.form_submit_button("Send Message")

if send_clicked and user_input.strip() != "":
    st.session_state.messages.append({"sender": "user", "text": user_input})
    response = get_bot_response(user_input)
    st.session_state.messages.append({"sender": "bot", "text": response})
    st.rerun()

# ---------------- BOTTOM ACTIONS ----------------

c1, c2 = st.columns(2)

with c1:
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {
                "sender": "bot",
                "text": "Chat cleared. How can I help you?"
            }
        ]
        st.rerun()

with c2:
    chat_text = "\n".join(
        [f"{msg['sender'].title()}: {msg['text']}" for msg in st.session_state.messages]
    )

    st.download_button(
        label="Download Chat",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )

st.markdown("""
<div class="footer">
Smart Assistant uses predefined rules and keyword matching to generate responses.
</div>
""", unsafe_allow_html=True)