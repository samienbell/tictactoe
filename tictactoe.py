def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")


def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_full(board):
    return all([spot != " " for row in board for spot in row])


def play_tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        # Get user input
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row and column: 0 1): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
            continue

        # Check if input is valid
        if row not in range(3) or col not in range(3):
            print("Invalid move. Please select row and column from 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("This spot is already taken. Try a different one.")
            continue

        # Make the move
        board[row][col] = current_player
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tictactoe()