\# Task 2: Tic-Tac-Toe AI



\## Project Title

Tic-Tac-Toe AI using Minimax Algorithm



\## Internship

CodSoft Artificial Intelligence Internship



\## Objective

The objective of this project is to implement an AI agent that plays Tic-Tac-Toe against a human player. The AI uses the Minimax algorithm in hard mode to choose the best possible move.



\## Description

This project is a Tic-Tac-Toe game where the human player plays as X and the AI plays as O.



The project includes two modes:

\- Easy Mode: The AI chooses random moves.

\- Hard Mode: The AI uses the Minimax algorithm to make optimal moves.



In hard mode, the AI checks all possible future moves and chooses the move with the best outcome. This makes the AI unbeatable. A perfect human player can only draw against the AI.



\## Features

\- Human vs AI gameplay

\- Easy mode with random AI moves

\- Hard mode with Minimax AI

\- Scoreboard for Player, AI, and Draws

\- New Round option

\- Reset Scores option

\- Streamlit frontend interface

\- Command-line version also included



\## Technologies Used

\- Python

\- Streamlit

\- Minimax Algorithm

\- Game Theory

\- Recursion



\## How Minimax Works

The Minimax algorithm evaluates all possible moves in the game.



The scoring system is:

\- AI win: +1

\- Human win: -1

\- Draw: 0



The AI tries to maximize the score, while the human player is assumed to minimize the AI's score. Based on this, the AI selects the best move.



\## How to Run Command-Line Version



```bash

python tic\_tac\_toe.py

