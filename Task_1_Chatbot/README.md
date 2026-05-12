

\## Step 1: Create README file



In Command Prompt, make sure you are inside:



```cmd

C:\\Users\\User\\CODSOFT\\Task\_1\_Chatbot>

```



Then type:



```cmd

notepad README.md

```



If Notepad asks to create a new file, click \*\*Yes\*\*.



\---



\## Step 2: Paste this README content



Paste this into `README.md`:



````markdown

\# Task 1: Chatbot with Rule-Based Responses



\## Project Title

Smart Student Assistant Chatbot



\## Internship

CodSoft Artificial Intelligence Internship



\## Objective

The objective of this project is to build a simple chatbot that responds to user inputs using predefined rules. The chatbot uses if-else statements and keyword matching techniques to identify user queries and provide suitable responses.



\## Description

This is a rule-based chatbot developed using Python. It does not use machine learning or any external AI model. The chatbot checks the user's input, converts it into lowercase, and searches for specific keywords. Based on the matched keyword, it gives a predefined response.



This project helped me understand the basics of natural language processing, text preprocessing, keyword matching, and conversation flow.



\## Features

\- Greets the user

\- Responds to name-related questions

\- Provides study tips

\- Gives internship guidance

\- Explains Python basics

\- Explains Artificial Intelligence

\- Gives GitHub and LinkedIn guidance

\- Shows current time

\- Shows current date

\- Tells jokes

\- Gives motivational quotes

\- Stores and displays chat history

\- Exits when the user types bye, exit, or quit

\- Gives fallback response for unknown inputs



\## Technologies Used

\- Python

\- If-else statements

\- Pattern matching

\- Lists

\- Functions

\- Random module

\- Datetime module



\## How It Works

1\. The chatbot starts with a welcome message.

2\. The user enters a message.

3\. The message is converted into lowercase.

4\. The chatbot checks the message using predefined rules.

5\. If a keyword matches, the chatbot gives the related response.

6\. If no keyword matches, the chatbot gives a fallback response.

7\. The chatbot continues running until the user types bye, exit, or quit.



\## How to Run

Open the terminal in the project folder and run:



```bash

python chatbot.py

````



\## Sample Inputs



You can try these inputs:



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



\## What I Learned



Through this task, I learned how basic chatbot systems work using rule-based logic. I understood how user input can be processed using lowercase conversion, keyword matching, if-else conditions, and predefined responses.



\## Conclusion



This chatbot is a beginner-friendly rule-based chatbot that demonstrates simple natural language processing and conversation flow using Python.



````



Save and close Notepad.



\---



\## Step 3: Check files



In Command Prompt, type:



```cmd

dir

````



You should see:



```text

chatbot.py

README.md

```



Your folder should now look like this:



```text

Task\_1\_Chatbot/

│

├── chatbot.py

└── README.md

```



\---



\## Step 4: Run one final test



Run:



```cmd

python chatbot.py

```



Test:



```text

hello

help

show history

bye

```





