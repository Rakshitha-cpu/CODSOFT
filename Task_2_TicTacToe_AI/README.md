# Task 2: Tic-Tac-Toe AI

## Project Title
Tic-Tac-Toe AI using Minimax Algorithm

## Internship
CodSoft Artificial Intelligence Internship

## Objective
The objective of this project is to build an AI agent that plays Tic-Tac-Toe against a human player. The AI uses the Minimax algorithm in Hard Mode to choose the best possible move.

## Description
This project is a Human vs AI Tic-Tac-Toe game built using Python.

The human player plays as **X** and the AI plays as **O**.

The project includes two difficulty modes:

- **Easy Mode:** AI makes random moves.
- **Hard Mode:** AI uses the Minimax algorithm to make optimal moves.

In Hard Mode, the AI checks all possible future moves and selects the move with the best outcome. Because of this, the AI is unbeatable. A perfect human player can only draw against it.

## Features
- Human vs AI gameplay
- Easy Mode with random AI moves
- Hard Mode with Minimax AI
- Scoreboard for Player, AI, and Draws
- New Round option
- Reset Scores option
- Command-line version
- Streamlit frontend version
- Game status messages
- Input validation in terminal version

## Technologies Used
- Python
- Streamlit
- Minimax Algorithm
- Recursion
- Game Theory
- Conditional Logic
- Lists and Functions

## How Minimax Works
Minimax is a decision-making algorithm used in two-player games.

The AI assumes that both players will play optimally. It checks all possible future moves and assigns scores to each outcome.

Scoring system:

| Result | Score |
|---|---|
| AI wins | +1 |
| Human wins | -1 |
| Draw | 0 |

The AI tries to maximize the score, while the human player is assumed to minimize the AI's score. The AI then selects the move with the highest score.

## Game Flow

```text
Start Game
    ↓
Human chooses a cell
    ↓
Check if Human wins or game is draw
    ↓
AI calculates best move
    ↓
AI places O
    ↓
Check if AI wins or game is draw
    ↓
Continue until win or draw
