#!/usr/bin/python3

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Check if the board is full (tie)."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """Get a valid row or column from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input! Enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")

        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ")
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ")

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue

        # Check winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
