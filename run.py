import gspread
from google.oauth2.service_account import Credentials
import random

# Google Sheets setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = '/workspace/battleships_pp3/creds.json'
SPREADSHEET_NAME = 'BattleshipsPP3'

credentials = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
client = gspread.authorize(credentials)
sheet = client.open(SPREADSHEET_NAME).sheet1

# Initialize the board
def initialize_board():
    # Create a 5x5 grid
    board = [['O' for _ in range(5)] for _ in range(5)]
    return board
	
# Print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Place the ship randomly on the board
def place_ship():
    return random.randint(0, 4), random.randint(0, 4)

# Update board in Google Sheet
def update_sheet(board):
    for i in range(5):
        sheet.update(f'A{i+1}:E{i+1}', [board[i]])

# Read board from Google Sheet 
def read_board_from_sheet():
    board_data = sheet.get('A1:E5')
    return board_data

# Get valid input from the user 
def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 4:
                return value
            else:
                print("Please enter a number between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Game logic for Battleships
def play_game():
    print("Welcome to Battleships!")
    
    board = initialize_board()  # Initialize a blank board
    ship_row, ship_col = place_ship()  # Place a random ship
    
    # Save initial board state to Google Sheets
    update_sheet(board)
    
    # Maximum guesses allowed
    max_turns = 5

    for turn in range(max_turns):
        print(f"\nTurn {turn + 1} of {max_turns}")
        print_board(board)
        
        # Get player's guess
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))
        
        # Check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            board[guess_row][guess_col] = "X"
            update_sheet(board)  # Update the board in Google Sheets
            break
        else:
            if 0 <= guess_row <= 4 and 0 <= guess_col <= 4:
                if board[guess_row][guess_col] == "X":
                    print("You already guessed that spot!")
                else:
                    print("You missed!")
                    board[guess_row][guess_col] = "X"
                    update_sheet(board)  # Update the board in Google Sheets
            else:
                print("That's not even in the ocean!")
        
        if turn == max_turns - 1:
            print("Game over! You ran out of turns.")
            print(f"The ship was at: ({ship_row}, {ship_col})")

# Run the game
if __name__ == '__main__':
    play_game()
