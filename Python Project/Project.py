import os
import pickle
import time

# Utility Functions
def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def display_board(board):
    """Displays the Tic Tac Toe board."""
    size = len(board)
    clear_screen()
    print("\nAdvanced Tic Tac Toe\n")
    for row in board:
        print(" | ".join(row))
        print("-" * (size * 4 - 1))


def initialize_board(size):
    """Initializes an empty board of given size."""
    return [[" " for _ in range(size)] for _ in range(size)]


# Gameplay Functions
def check_winner(board, player):
    """Checks if the given player has won."""
    size = len(board)

    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or all(board[j][i] == player for j in range(size)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(size)) or all(board[i][size - i - 1] == player for i in range(size)):
        return True

    return False


def is_draw(board):
    """Checks if the board is full, resulting in a draw."""
    return all(all(cell != " " for cell in row) for row in board)


def get_player_move(board, player_name):
    """Prompts the player for a valid move."""
    size = len(board)
    while True:
        try:
            move = int(input(f"{player_name}, enter your move (1-{size*size}): ")) - 1
            row, col = divmod(move, size)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and", size * size)


# AI Functions
def minimax(board, depth, is_maximizing, ai_symbol, player_symbol):
    """Implements the minimax algorithm for AI."""
    if check_winner(board, ai_symbol):
        return 10 - depth
    if check_winner(board, player_symbol):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    board[i][j] = ai_symbol
                    score = minimax(board, depth + 1, False, ai_symbol, player_symbol)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    board[i][j] = player_symbol
                    score = minimax(board, depth + 1, True, ai_symbol, player_symbol)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score


def get_ai_move(board, ai_symbol, player_symbol):
    """Determines the AI's move using minimax."""
    best_score = float("-inf")
    best_move = None

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = ai_symbol
                score = minimax(board, 0, False, ai_symbol, player_symbol)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


# Main Game Functions
def play_game(grid_size, mode, player1, player2):
    """Plays a single Tic Tac Toe game."""
    board = initialize_board(grid_size)
    players = [player1, player2]
    symbols = ["X", "O"]
    current_player = 0

    while True:
        display_board(board)
        print(f"{players[current_player]}'s turn ({symbols[current_player]}).")

        if mode == "PvP" or (mode == "PvAI" and current_player == 0):
            row, col = get_player_move(board, players[current_player])
        else:
            print("AI is thinking...")
            row, col = get_ai_move(board, symbols[1], symbols[0])

        board[row][col] = symbols[current_player]

        if check_winner(board, symbols[current_player]):
            display_board(board)
            print(f"{players[current_player]} wins!")
            return players[current_player]
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            return "Draw"

        current_player = 1 - current_player


def save_game(scores):
    """Saves the current scoreboard to a file."""
    with open("scores.pkl", "wb") as f:
        pickle.dump(scores, f)


def load_game():
    """Loads the scoreboard from a file."""
    try:
        with open("scores.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {"Player 1": 0, "Player 2": 0, "AI": 0, "Draws": 0}


# Main Menu
def main_menu():
    """Displays the main menu."""
    scores = load_game()
    while True:
        clear_screen()
        print("Advanced Tic Tac Toe\n")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. View Scores")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name1 = input("Enter Player 1's name: ")
            name2 = input("Enter Player 2's name: ")
            winner = play_game(3, "PvP", name1, name2)
            if winner != "Draw":
                scores[winner] = scores.get(winner, 0) + 1
            else:
                scores["Draws"] += 1
            save_game(scores)

        elif choice == "2":
            name = input("Enter your name: ")
            winner = play_game(3, "PvAI", name, "AI")
            if winner == "AI":
                scores["AI"] += 1
            elif winner == name:
                scores[name] = scores.get(name, 0) + 1
            else:
                scores["Draws"] += 1
            save_game(scores)

        elif choice == "3":
            clear_screen()
            print("Scores:\n")
            for player, score in scores.items():
                print(f"{player}: {score}")
            input("\nPress Enter to return to the main menu.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the Program
if __name__ == "__main__":
    main_menu()
