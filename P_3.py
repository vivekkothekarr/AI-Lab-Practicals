def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

def main():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are 0-8 starting from top-left.")
    
    for turn in range(9):
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter position (0-8): "))
            if board[move] != " ":
                print("Space already taken! Try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("Invalid input! Use numbers 0-8.")
            continue

        winner = check_win(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    main()