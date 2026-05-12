import datetime
import random

chat_history = []

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


def show_help():
    print("\nBot: You can ask me about:")
    print("1. Greetings")
    print("2. My name")
    print("3. Study tips")
    print("4. Internship guidance")
    print("5. Python learning")
    print("6. Artificial Intelligence")
    print("7. GitHub guidance")
    print("8. LinkedIn guidance")
    print("9. Time")
    print("10. Date")
    print("11. Joke")
    print("12. Motivation")
    print("13. Chat history")
    print("14. Exit\n")


def show_history():
    if len(chat_history) == 0:
        print("Bot: No chat history available yet.")
    else:
        print("\nBot: Your chat history:")
        for index, message in enumerate(chat_history, start=1):
            print(index, "-", message)
        print()


print("Bot: Hello! I am Smart Student Assistant Chatbot.")
print("Bot: I respond using predefined rules and keyword matching.")
print("Bot: Type 'help' to see what I can do.")

while True:
    user_input = input("\nYou: ").lower()
    chat_history.append(user_input)

    if any(word in user_input for word in greetings):
        responses = [
            "Hello! How can I help you today?",
            "Hi! What do you want to learn?",
            "Hey! I am ready to help you."
        ]
        print("Bot:", random.choice(responses))

    elif any(word in user_input for word in farewells):
        print("Bot: Goodbye! Keep learning and keep building projects.")
        break

    elif "help" in user_input:
        show_help()

    elif any(word in user_input for word in name_questions):
        print("Bot: I am Smart Student Assistant, a rule-based chatbot created using Python.")

    elif "how are you" in user_input:
        print("Bot: I am working perfectly. I am ready to answer your questions.")

    elif any(word in user_input for word in study_keywords):
        print("Bot: Study tip: Make a daily plan, revise regularly, and practice problems instead of only reading theory.")

    elif any(word in user_input for word in internship_keywords):
        print("Bot: Internship tip: Complete tasks properly, upload them on GitHub, record demo videos, and explain your project clearly.")

    elif any(word in user_input for word in python_keywords):
        print("Bot: Python tip: Learn variables, conditions, loops, functions, lists, and file handling. Then build small projects.")

    elif any(word in user_input for word in ai_keywords):
        print("Bot: Artificial Intelligence means making machines perform tasks that usually require human intelligence.")

    elif any(word in user_input for word in github_keywords):
        print("Bot: GitHub tip: Create a clean repository, add task folders, upload code, and write a proper README file.")

    elif any(word in user_input for word in linkedin_keywords):
        print("Bot: LinkedIn tip: Post your demo video, explain what you built, tag CodSoft, and use relevant hashtags.")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "joke" in user_input:
        print("Bot:", random.choice(jokes))

    elif "motivation" in user_input or "quote" in user_input:
        print("Bot:", random.choice(quotes))

    elif "history" in user_input:
        show_history()

    else:
        print("Bot: I don't have a rule for that yet. Try typing 'help'.")