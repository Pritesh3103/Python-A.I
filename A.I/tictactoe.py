import random

# Constants
EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    """Check if the given player has won."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)               # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(cell != EMPTY for cell in board)

def get_available_moves(board):
    """Return a list of available moves."""
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to find the best move for AI."""
    if check_winner(board, PLAYER_X):
        return -10
    elif check_winner(board, PLAYER_O):
        return 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Find the best move for the AI."""
    best_score = -float('inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = PLAYER_O
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    """Play the Tic-Tac-Toe game."""
    board = [EMPTY] * 9
    current_player = PLAYER_X

    while True:
        print_board(board)
        if current_player == PLAYER_X:
            move = int(input("Enter your move (0-8): "))
            if board[move] != EMPTY:
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is making a move...")
            move = find_best_move(board)

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    play_game()
