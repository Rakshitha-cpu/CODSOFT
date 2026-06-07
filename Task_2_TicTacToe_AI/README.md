<div align="center">

```
 ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
    ██╔══╝██║██╔════╝       ██╔══╝██╔══██╗██╔════╝       ██╔══╝██╔═══██╗██╔════╝
    ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗
    ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝
    ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
    ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
                                   A I
```

# 🎮 Tic-Tac-Toe AI — Minimax Algorithm

> **CodSoft Artificial Intelligence Internship | Task 2**
> An unbeatable AI agent built with Python using the Minimax algorithm

<br/>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-Minimax-green?style=for-the-badge)
![Mode](https://img.shields.io/badge/Mode-Hard%20%7C%20Easy-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

---

## 📌 Project Overview

This project is part of the **CodSoft Artificial Intelligence Internship**, implementing a fully functional **Human vs AI Tic-Tac-Toe** game. The AI leverages the **Minimax Algorithm** in Hard Mode to compute optimal moves — making it theoretically **unbeatable**.

- 🧑 Human plays as **X**
- 🤖 AI plays as **O**
- 🧠 In Hard Mode: AI never loses — the best a human can achieve is a **draw**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎮 Human vs AI Gameplay | Interactive turn-based game |
| 🟢 Easy Mode | AI makes **random** moves |
| 🔴 Hard Mode | AI uses **Minimax** for optimal play |
| 📊 Scoreboard | Tracks Player, AI, and Draw counts |
| 🔄 New Round | Start a fresh game without resetting scores |
| 🔁 Reset Scores | Clear the entire scoreboard |
| 💻 CLI Version | Terminal-based gameplay with input validation |
| 🌐 Web Version | Beautiful Streamlit frontend |
| 📢 Game Status | Real-time messages for moves, wins, and draws |

---

## 🧠 How Minimax Works

> *"The AI sees every possible future — and always chooses the best one."*

**Minimax** is a recursive, tree-based decision-making algorithm used in two-player zero-sum games. The AI simulates all possible game states and picks the move with the highest score under the assumption that **both players play optimally**.

### Scoring System

```
╔══════════════════════╦═════════╗
║       Outcome        ║  Score  ║
╠══════════════════════╬═════════╣
║   🤖 AI Wins (O)     ║   +1    ║
║   🧑 Human Wins (X)  ║   -1    ║
║   🤝 Draw            ║    0    ║
╚══════════════════════╩═════════╝
```

### AI Decision Logic

```python
def minimax(board, is_maximizing):
    # Base cases: check win/draw
    if ai_wins():    return +1
    if human_wins(): return -1
    if draw():       return  0

    if is_maximizing:
        best = -infinity
        for move in available_moves:
            score = minimax(board_with_move, False)
            best = max(best, score)
        return best
    else:
        best = +infinity
        for move in available_moves:
            score = minimax(board_with_move, True)
            best = min(best, score)
        return best
```

The AI **maximizes** its own score while assuming the human will **minimize** it.

---

## 🔄 Game Flow

```
                    ┌─────────────┐
                    │  Start Game │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Human Turn │  ← Human places X
                    └──────┬──────┘
                           │
             ┌─────────────▼──────────────┐
             │  Check: Human Win or Draw?  │
             └──────┬───────────┬──────────┘
                    │ No        │ Yes
                    │           └──► 🏆 Game Over
                    │
             ┌──────▼──────────────────────┐
             │  AI Calculates Best Move     │  ← Minimax runs
             │  (via Minimax Algorithm)     │
             └──────┬──────────────────────┘
                    │
                    │  AI places O
                    │
             ┌──────▼──────────────────────┐
             │  Check: AI Win or Draw?      │
             └──────┬───────────┬───────────┘
                    │ No        │ Yes
                    │           └──► 🏆 Game Over
                    │
                    └──► (Back to Human Turn)
```

---

## 🗂️ Project Structure

```
tic-tac-toe-ai/
│
├── 📄 tictactoe.py          # Core game logic + Minimax algorithm
├── 📄 app.py                # Streamlit web frontend
├── 📄 requirements.txt      # Python dependencies
└── 📄 README.md             # Project documentation
```

---

## ⚙️ Technologies Used

```
┌────────────────────────────────────────────────────────┐
│  🐍  Python          Core language                     │
│  🌐  Streamlit       Web-based frontend UI             │
│  🧠  Minimax         Decision-making algorithm         │
│  🔁  Recursion       Tree traversal for game states    │
│  ♟️  Game Theory     Optimal strategy framework        │
│  📋  Lists           Board state representation        │
│  🔀  Functions       Modular, clean code structure     │
└────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.x
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai

# 2. Install dependencies
pip install -r requirements.txt
```

### Run the Game

#### 💻 Command-Line Version

```bash
python tictactoe.py
```

#### 🌐 Streamlit Web Version

```bash
streamlit run app.py
```

---

## 🎮 How to Play

```
1. Choose your difficulty: Easy (random AI) or Hard (Minimax AI)
2. You are X  —  AI is O
3. Enter the position (1–9) to place your mark:

        1 │ 2 │ 3
       ───┼───┼───
        4 │ 5 │ 6
       ───┼───┼───
        7 │ 8 │ 9

4. The AI responds with its best move
5. First to align 3 marks wins — or it's a draw!
```

---
#ScreenShots

<img width="1280" height="612" alt="image" src="https://github.com/user-attachments/assets/a9b19736-f95f-4885-ae95-c811ec82d86d" />
<img width="1280" height="612" alt="image" src="https://github.com/user-attachments/assets/0ba09581-c659-442d-9f68-34b91103a1df" />
<img width="1280" height="612" alt="image" src="https://github.com/user-attachments/assets/0000d79e-bf85-44d4-910d-71d18c78e5cc" />

----



---

## 🧪 AI Difficulty Modes

### 🟢 Easy Mode — Random AI

```python
import random

def easy_move(board):
    empty_cells = [i for i, v in enumerate(board) if v == ' ']
    return random.choice(empty_cells)
```

> The AI picks a random available cell. Beatable with basic strategy.

---

### 🔴 Hard Mode — Minimax AI

```python
def best_move(board):
    best_score = -infinity
    move = None
    for cell in available_moves(board):
        board[cell] = 'O'
        score = minimax(board, is_maximizing=False)
        board[cell] = ' '
        if score > best_score:
            best_score = score
            move = cell
    return move
```

> The AI evaluates every future game state. **Impossible to beat.**

---

## 📊 Scoreboard Preview

```
╔══════════════════════════════╗
║         SCOREBOARD           ║
╠═══════════╦══════╦═══════════╣
║  🧑 You   ║  🤝  ║  🤖 AI   ║
╠═══════════╬══════╬═══════════╣
║     2     ║  3   ║     5     ║
╚═══════════╩══════╩═══════════╝
```

---

## 🏆 Why the AI is Unbeatable

In Hard Mode, the Minimax algorithm explores the **complete game tree** — every possible sequence of moves for both players. With only 9 cells, there are at most **9! = 362,880** possible game sequences, which the algorithm evaluates exhaustively.

Because the AI always picks the move with the best guaranteed outcome:
- If a win is possible → AI **wins**
- If a win isn't possible → AI **forces a draw**
- The AI **never loses** against any strategy

> 💡 A perfect human player can only achieve a **draw** — never a win.

---

## 👤 Author

**Internship:** CodSoft Artificial Intelligence Internship
**Task:** Task 2 — Tic-Tac-Toe AI using Minimax Algorithm
**Stack:** Python · Streamlit · Minimax · Game Theory

---

## 📄 License

This project is created for educational and internship purposes under **CodSoft**.

---

<div align="center">

*Built with ❤️ and the Minimax Algorithm*

*"In a perfect game, the best you can do against a perfect opponent — is draw."*

</div>
