import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to make the computer's move
def make_computer_move(board, computer, player):
    # Check if the computer can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = computer
                if check_winner(board, computer):
                    return

                board[row][col] = ' '

    # Check if the player can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                if check_winner(board, player):
                    board[row][col] = computer
                    return

                board[row][col] = ' '

    # Choose a random empty cell
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = computer

# Function to play the Tic-Tac-Toe game
def play_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    players = ['X', 'O']
    current_player = random.choice(players)
    
    player=current_player
    computer = 'O' if player == 'X' else 'X'

    print("Tic-Tac-Toe Game - You are '{}'".format(current_player))
    print_board(board)

    while True:
        if current_player == player:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if board[row][col] != ' ':
                print("Invalid move! Try again.")
                continue

            board[row][col] = current_player

        else:
            make_computer_move(board, computer, player)

        print_board(board)

        if check_winner(board, current_player):
            print("Player '{}' wins!".format(current_player))
            break

        if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()