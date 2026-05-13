# Tic-Tac-Toe AI using Minimax Algorithm
# Human Player = X
# AI Player = O

board = [" " for _ in range(9)]


def print_positions():
    print("\nBoard Positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # middle column
        [2, 5, 8],  # right column
        [0, 4, 8],  # diagonal
        [2, 4, 6]   # diagonal
    ]

    for combination in winning_combinations:
        if (
            board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player
        ):
            return True

    return False


def check_draw():
    return " " not in board


def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid move. Choose a number from 1 to 9.")

            elif board[move] != " ":
                print("That position is already taken. Choose another position.")

            else:
                board[move] = "X"
                break

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")


def minimax(is_ai_turn):
    # Base conditions
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if check_draw():
        return 0

    # AI turn: maximize score
    if is_ai_turn:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "

                if score > best_score:
                    best_score = score

        return best_score

    # Human turn: minimize AI score
    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "

                if score < best_score:
                    best_score = score

        return best_score


def ai_move():
    best_score = -100
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"
    print("AI placed O at position", best_move + 1)


def play_game():
    print("===================================")
    print("        TIC-TAC-TOE AI GAME        ")
    print("===================================")
    print("You are X")
    print("AI is O")
    print("AI uses Minimax Algorithm")
    print("Try to beat the AI!")
    print_positions()

    while True:
        print_board()

        # Human move
        human_move()

        if check_winner("X"):
            print_board()
            print("Congratulations! You win!")
            break

        if check_draw():
            print_board()
            print("Game Draw!")
            break

        # AI move
        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins! You cannot beat perfect Minimax AI.")
            break

        if check_draw():
            print_board()
            print("Game Draw!")
            break


play_game()