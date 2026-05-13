
````markdown
# 🎮 Task 2: Tic-Tac-Toe AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Minimax](https://img.shields.io/badge/Algorithm-Minimax-7C3AED?style=for-the-badge)
![Game AI](https://img.shields.io/badge/AI-Game%20Agent-FF6F61?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![CodSoft](https://img.shields.io/badge/Internship-CodSoft-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-28a745?style=for-the-badge)

**An AI-powered Tic-Tac-Toe game built using Python and the Minimax algorithm**

</div>

---

## 📌 Project Overview

| Field | Details |
|---|---|
| 🏷️ Project Name | Tic-Tac-Toe AI |
| 🏢 Internship | CodSoft Artificial Intelligence Internship |
| 📁 Task | Task 2 — Tic-Tac-Toe AI |
| 💻 Language | Python |
| 🧠 Algorithm | Minimax Algorithm |
| 🎮 Game Type | Human vs AI |
| 🖥️ Interface | Command Line + Streamlit Frontend |

---

## 🎯 Objective

> Implement an AI agent that plays the classic game of **Tic-Tac-Toe** against a human player.

The goal of this project is to understand how an AI can make decisions in a game environment using **game theory** and **search algorithms**.

In this project, the AI uses the **Minimax algorithm** in Hard Mode to calculate the best possible move, making it unbeatable.

---

## 📖 Description

This project is a **Human vs AI Tic-Tac-Toe game**.

The human player plays as:

```text
X
````

The AI player plays as:

```text
O
```

The project includes two difficulty modes:

| Mode      | AI Behavior                                              |
| --------- | -------------------------------------------------------- |
| Easy Mode | AI selects random available moves                        |
| Hard Mode | AI uses the Minimax algorithm to choose the optimal move |

In **Hard Mode**, the AI checks all possible future moves and selects the move with the best outcome. Because of this, the AI cannot be beaten if it plays optimally.

A perfect human player can only force a draw.

---

## ✨ Features

| #  | Feature                  | Description                                |
| -- | ------------------------ | ------------------------------------------ |
| 1  | 🎮 Human vs AI Gameplay  | Player competes against the computer       |
| 2  | ❌ Player Symbol          | Human player uses X                        |
| 3  | ⭕ AI Symbol              | AI uses O                                  |
| 4  | 🧠 Minimax Algorithm     | AI calculates the best possible move       |
| 5  | 🎲 Easy Mode             | AI makes random moves                      |
| 6  | 🔥 Hard Mode             | AI becomes unbeatable using Minimax        |
| 7  | 🏆 Scoreboard            | Tracks Player, AI, and Draw scores         |
| 8  | 🔁 New Round             | Restart the board without resetting scores |
| 9  | ♻️ Reset Scores          | Clears all scores and starts fresh         |
| 10 | 🖥️ Command-Line Version | Play directly in the terminal              |
| 11 | 🌐 Streamlit Frontend    | Play using a simple graphical interface    |
| 12 | 🧩 Game Status Messages  | Shows win, lose, draw, and turn messages   |
| 13 | ✅ Input Validation       | Prevents invalid moves in terminal version |
| 14 | 📚 Game Theory Concept   | Demonstrates decision-making using search  |

---

## 🛠️ Technologies Used

```text
✅ Python 3.x
✅ Streamlit
✅ Minimax Algorithm
✅ Recursion
✅ Game Theory
✅ Conditional Logic
✅ Lists
✅ Functions
```

---

## 🧠 What is Minimax?

The **Minimax algorithm** is a decision-making algorithm used in two-player games.

It assumes:

```text
AI tries to maximize its score.
Human tries to minimize the AI's score.
```

The AI explores possible future moves and chooses the move that gives the best result.

---

## ⚙️ Minimax Scoring System

| Game Result | Score |
| ----------- | ----- |
| AI Wins     | +1    |
| Human Wins  | -1    |
| Draw        | 0     |

The AI checks every possible move and selects the move with the highest score.

---

## 🔍 How the AI Thinks

```text
Current Board
    │
    ▼
Check Available Moves
    │
    ▼
Simulate AI Move
    │
    ▼
Simulate Human Response
    │
    ▼
Evaluate Result
    │
    ├── AI Win    → +1
    ├── Human Win → -1
    └── Draw      → 0
    │
    ▼
Choose Move with Best Score
```

---

## 🧩 Game Logic Flow

```text
Start Game
    │
    ▼
Display Board
    │
    ▼
Human Chooses a Cell
    │
    ▼
Check Human Win / Draw
    │
    ▼
AI Calculates Move
    │
    ▼
AI Places O
    │
    ▼
Check AI Win / Draw
    │
    ▼
Continue Until Win or Draw
```

---

## 🚀 How to Run

### ▶️ Run Command-Line Version

**Step 1 — Navigate to project folder:**

```bash
cd Task_2_TicTacToe_AI
```

**Step 2 — Run the Python file:**

```bash
python tic_tac_toe.py
```

---

### 🌐 Run Streamlit Frontend

**Step 1 — Install Streamlit if not installed:**

```bash
pip install streamlit
```

**Step 2 — Run the frontend app:**

```bash
python -m streamlit run app.py
```

---

## 🎮 How to Play

The board positions are:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

Rules:

```text
1. Human plays as X.
2. AI plays as O.
3. Human chooses an empty cell.
4. AI makes its move.
5. First player to get 3 symbols in a row wins.
6. If all cells are filled and nobody wins, the game is a draw.
```

Winning can happen through:

```text
Rows
Columns
Diagonals
```

---

## 📂 Project Structure

```text
Task_2_TicTacToe_AI/
│
├── tic_tac_toe.py     ← Command-line Tic-Tac-Toe AI game
├── app.py             ← Streamlit frontend version
└── README.md          ← Project documentation
```

---

## 🧪 Sample Gameplay

```text
Tic-Tac-Toe AI Game
You are X
AI is O
AI uses Minimax Algorithm

Enter your move (1-9): 5
AI placed O at position 1

Enter your move (1-9): 9
AI placed O at position 3
```

In Hard Mode, the AI always chooses the optimal move using Minimax.

---

## 📚 What I Learned

* ✅ How AI can make decisions in games
* ✅ How the Minimax algorithm works
* ✅ How recursion is used in decision trees
* ✅ How to evaluate game states using scores
* ✅ How to create an unbeatable AI agent
* ✅ Difference between random AI and intelligent AI
* ✅ How to build both terminal and frontend versions
* ✅ How game theory applies to real AI problems

---

## ⚠️ Limitations

This project is based on the classic 3x3 Tic-Tac-Toe game.

The Minimax algorithm works perfectly here because Tic-Tac-Toe has a small number of possible moves. For larger games like Chess, Minimax needs optimizations such as:

```text
Alpha-Beta Pruning
Depth Limiting
Heuristic Evaluation
```

---

## 🏁 Conclusion

This **Tic-Tac-Toe AI** project demonstrates how an AI agent can make intelligent decisions using the Minimax algorithm.

The project helped me understand the fundamentals of:

```text
Game Theory
Search Algorithms
Recursion
AI Decision Making
```

In Easy Mode, the AI behaves randomly.
In Hard Mode, the AI uses Minimax and becomes unbeatable.

---

<div align="center">

Made with ❤️ by **Rakshitha R** | CodSoft AI Internship

</div>
```


```
