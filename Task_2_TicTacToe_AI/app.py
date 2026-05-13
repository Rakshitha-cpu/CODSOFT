import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Tic-Tac-Toe AI",
    page_icon="🎮",
    layout="centered"
)

# ---------------- CONSTANTS ----------------

HUMAN = "X"
AI = "O"
EMPTY = " "

WINNING_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

# ---------------- GAME LOGIC ----------------

def check_winner(board, player):
    for combo in WINNING_COMBINATIONS:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False


def check_draw(board):
    return EMPTY not in board


def get_status(board):
    if check_winner(board, HUMAN):
        return "human"
    if check_winner(board, AI):
        return "ai"
    if check_draw(board):
        return "draw"
    return "playing"


def minimax(board, is_ai_turn):
    status = get_status(board)

    if status == "ai":
        return 1
    if status == "human":
        return -1
    if status == "draw":
        return 0

    if is_ai_turn:
        best_score = -100

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best_score = min(best_score, score)

        return best_score


def get_best_ai_move(board):
    best_score = -100
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def get_random_ai_move(board):
    empty_cells = [i for i in range(9) if board[i] == EMPTY]
    return random.choice(empty_cells) if empty_cells else None


def reset_board():
    st.session_state.board = [EMPTY for _ in range(9)]
    st.session_state.game_over = False
    st.session_state.message = "Your turn. Choose a cell."


def reset_scores():
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.draw_score = 0
    reset_board()


def ai_turn():
    if st.session_state.difficulty == "Easy":
        move = get_random_ai_move(st.session_state.board)
    else:
        move = get_best_ai_move(st.session_state.board)

    if move is not None:
        st.session_state.board[move] = AI

    status = get_status(st.session_state.board)

    if status == "ai":
        st.session_state.ai_score += 1
        st.session_state.game_over = True
        st.session_state.message = "AI wins. Try again!"

    elif status == "draw":
        st.session_state.draw_score += 1
        st.session_state.game_over = True
        st.session_state.message = "Draw. Good game!"

    else:
        st.session_state.message = "Your turn. Choose a cell."


def human_turn(index):
    if st.session_state.game_over:
        return

    if st.session_state.board[index] != EMPTY:
        return

    st.session_state.board[index] = HUMAN

    status = get_status(st.session_state.board)

    if status == "human":
        st.session_state.player_score += 1
        st.session_state.game_over = True
        st.session_state.message = "You win. Nice move!"

    elif status == "draw":
        st.session_state.draw_score += 1
        st.session_state.game_over = True
        st.session_state.message = "Draw. Well played!"

    else:
        ai_turn()

# ---------------- SESSION STATE ----------------

if "board" not in st.session_state:
    st.session_state.board = [EMPTY for _ in range(9)]

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = "Your turn. Choose a cell."

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Hard"

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "ai_score" not in st.session_state:
    st.session_state.ai_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0

if "theme" not in st.session_state:
    st.session_state.theme = "Blue"

# ---------------- THEME COLORS ----------------

themes = {
    "Blue": {
        "bg1": "#e0f2fe",
        "bg2": "#eef2ff",
        "primary": "#2563eb",
        "secondary": "#7c3aed",
        "human": "#2563eb",
        "ai": "#db2777"
    },
    "Purple": {
        "bg1": "#f3e8ff",
        "bg2": "#eef2ff",
        "primary": "#7c3aed",
        "secondary": "#ec4899",
        "human": "#7c3aed",
        "ai": "#e11d48"
    },
    "Green": {
        "bg1": "#dcfce7",
        "bg2": "#f0fdf4",
        "primary": "#16a34a",
        "secondary": "#059669",
        "human": "#16a34a",
        "ai": "#dc2626"
    },
    "Orange": {
        "bg1": "#ffedd5",
        "bg2": "#fff7ed",
        "primary": "#ea580c",
        "secondary": "#f97316",
        "human": "#ea580c",
        "ai": "#be123c"
    }
}

selected_theme = themes[st.session_state.theme]

# ---------------- CSS ----------------

st.markdown(f"""
<style>

.stApp {{
    background: linear-gradient(135deg, {selected_theme["bg1"]}, {selected_theme["bg2"]});
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

.block-container {{
    max-width: 850px;
    padding-top: 30px;
    padding-bottom: 30px;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

.main-title {{
    text-align: center;
    font-size: 44px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 5px;
}}

.subtitle {{
    text-align: center;
    font-size: 16px;
    color: #4b5563;
    margin-bottom: 25px;
}}

.status-box {{
    background: linear-gradient(135deg, {selected_theme["primary"]}, {selected_theme["secondary"]});
    color: white;
    padding: 16px;
    border-radius: 18px;
    text-align: center;
    font-weight: 900;
    font-size: 18px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.18);
}}

.score-card {{
    background: white;
    padding: 18px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
}}

.score-label {{
    font-size: 13px;
    color: #6b7280;
    font-weight: 900;
    margin-bottom: 6px;
}}

.score-value {{
    font-size: 34px;
    color: #111827;
    font-weight: 900;
}}

.board-title {{
    font-size: 18px;
    font-weight: 900;
    color: #111827;
    margin-top: 20px;
    margin-bottom: 12px;
}}

.stButton > button {{
    width: 100%;
    min-height: 82px;
    border-radius: 20px !important;
    background: white !important;
    color: #111827 !important;
    border: 2px solid #e5e7eb !important;
    font-size: 34px !important;
    font-weight: 900 !important;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
}}

.stButton > button:hover {{
    background: #f8fafc !important;
    border: 2px solid {selected_theme["primary"]} !important;
    transform: translateY(-2px);
}}

.small-button button {{
    min-height: 50px !important;
    font-size: 15px !important;
}}

.stSelectbox label, .stRadio label {{
    font-weight: 900 !important;
    color: #111827 !important;
}}

.footer-text {{
    text-align: center;
    color: #4b5563;
    font-size: 13px;
    margin-top: 20px;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------

st.markdown('<div class="main-title">🎮 Tic-Tac-Toe AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Play against an AI using Easy Random Mode or Hard Minimax Mode</div>', unsafe_allow_html=True)

top1, top2, top3 = st.columns([1, 1, 1])

with top1:
    theme_choice = st.selectbox(
        "Theme",
        ["Blue", "Purple", "Green", "Orange"],
        index=["Blue", "Purple", "Green", "Orange"].index(st.session_state.theme)
    )

    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()

with top2:
    difficulty_choice = st.selectbox(
        "Difficulty",
        ["Easy", "Hard"],
        index=1 if st.session_state.difficulty == "Hard" else 0
    )

    if difficulty_choice != st.session_state.difficulty:
        st.session_state.difficulty = difficulty_choice
        reset_board()
        st.rerun()

with top3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="status-box">{st.session_state.message}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

score1, score2, score3 = st.columns(3)

with score1:
    st.markdown(
        f'<div class="score-card"><div class="score-label">PLAYER</div><div class="score-value">{st.session_state.player_score}</div></div>',
        unsafe_allow_html=True
    )

with score2:
    st.markdown(
        f'<div class="score-card"><div class="score-label">AI</div><div class="score-value">{st.session_state.ai_score}</div></div>',
        unsafe_allow_html=True
    )

with score3:
    st.markdown(
        f'<div class="score-card"><div class="score-label">DRAWS</div><div class="score-value">{st.session_state.draw_score}</div></div>',
        unsafe_allow_html=True
    )

st.markdown('<div class="board-title">Game Board</div>', unsafe_allow_html=True)

for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        index = row * 3 + col
        value = st.session_state.board[index]

        if value == HUMAN:
            label = "❌"
        elif value == AI:
            label = "⭕"
        else:
            label = str(index + 1)

        with cols[col]:
            clicked = st.button(
                label,
                key=f"cell_{index}",
                use_container_width=True,
                disabled=st.session_state.game_over or value != EMPTY
            )

            if clicked:
                human_turn(index)
                st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

action1, action2 = st.columns(2)

with action1:
    st.markdown('<div class="small-button">', unsafe_allow_html=True)
    if st.button("New Round", use_container_width=True):
        reset_board()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with action2:
    st.markdown('<div class="small-button">', unsafe_allow_html=True)
    if st.button("Reset Scores", use_container_width=True):
        reset_scores()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer-text">Hard mode uses the Minimax algorithm to choose the best possible move.</div>',
    unsafe_allow_html=True
)