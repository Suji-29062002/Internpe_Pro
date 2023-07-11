# Tic-Tac-Toe
print("")
print("⭐ TIC-TAC-TOE ⭐")
print("")

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board0
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if any player has won
def check_winner(player):
    # Check rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    # Check columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Main game loop
current_player = 'X'
while True:
    print_board()
    print("It's player", current_player, "'s turn.")

    # Get the player's move
    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit() and int(move) >= 0 and int(move) <= 8 and board[int(move)] == ' ':
            break
        print("Invalid move. Try again.")

    # Update the board
    board[int(move)] = current_player

    # Check for a win
    if check_winner(current_player):
        print_board()
        print("Player", current_player, "wins!")
        break

    # Check for a tie
    if is_board_full():
        print_board()
        print("It's a tie!")
        break

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'
