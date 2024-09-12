import gspread
from google.oauth2.service_account import Credentials
import random
import sys

# Google Sheets setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = 'creds.json'
SPREADSHEET_NAME = 'BattleshipsPP3'

credentials = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
client = gspread.authorize(credentials)
sheet = client.open(SPREADSHEET_NAME).sheet1

# Initialize the board
def initialize_board():
    return [['O' for _ in range(5)] for _ in range(5)]

# Print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Display the player's and computer's boards side by side
def display_boards(player_board, computer_board):
    print("\nPlayer's Board         Computer's Board")
    print("----------------      -----------------")
    for i in range(5):
        # Display player and computer boards in two columns
        print(" ".join(player_board[i]) + "        " + " ".join(computer_board[i]))

# Place ships randomly on the board
def place_ships(num_ships=3):
    ships = set()
    while len(ships) < num_ships:
        row, col = random.randint(0, 4), random.randint(0, 4)
        ships.add((row, col))  # Add unique ship positions
    return list(ships)

# Update board in Google Sheet
def update_sheet(board, sheet_range):
    for i in range(5):
        sheet.update(f'{sheet_range}{i+1}:{chr(ord(sheet_range)+4)}{i+1}', [board[i]])

# Get valid input from the user (Bug Fix)
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

# Random guess for computer player
def computer_guess():
    return random.randint(0, 4), random.randint(0, 4)

# Check if all ships are sunk
def all_ships_sunk(ships, board):
    for ship_row, ship_col in ships:
        if board[ship_row][ship_col] != "X":  # Not hit yet
            return False
    return True

# Game logic for Battleships (Player vs Computer)
def play_game():
    print("Starting the Battleships game: Player vs Computer!")

    # Initialize boards
    player_board = initialize_board()  # Player's guesses
    computer_board = initialize_board()  # Computer's guesses
    player_ship_board = initialize_board()  # Player's ships
    computer_ship_board = initialize_board()  # Computer's ships

    # Place 3 ships for both the player and the computer
    player_ships = place_ships(3)  # Player's 3 ships
    computer_ships = place_ships(3)  # Computer's 3 ships

    # Mark the player's ships on the player board (not shown to the computer)
    for row, col in player_ships:
        player_ship_board[row][col] = "S"

    # Update initial boards to Google Sheets
    update_sheet(player_board, 'A')  # Player's guesses
    update_sheet(computer_board, 'G')  # Computer's guesses
    update_sheet(player_ship_board, 'M')  # Player's ships
    update_sheet(computer_ship_board, 'S')  # Computer's ships

    # Loop until one player wins (all ships of one side are sunk)
    while True:
        # Show current board state
        display_boards(player_board, computer_board)

        # --- Player's Turn ---
        print("Your turn:")
        guess_row = get_valid_input("Guess Row (0-4): ")
        guess_col = get_valid_input("Guess Col (0-4): ")

        # Check if the player's guess hits any of the computer's ships
        if (guess_row, guess_col) in computer_ships:
            print("Hit! You sunk part of the computer's ship!")
            player_board[guess_row][guess_col] = "X"
            update_sheet(player_board, 'A')
        else:
            if player_board[guess_row][guess_col] == "X":
                print("You already guessed that spot!")
            else:
                print("You missed!")
                player_board[guess_row][guess_col] = "X"
                update_sheet(player_board, 'A')

        # Check if player sunk all computer's ships
        if all_ships_sunk(computer_ships, player_board):
            print("Congratulations! You sunk all the computer's ships!")
            break

        # --- Computer's Turn ---
        print("Computer's turn...")
        comp_guess_row, comp_guess_col = computer_guess()

        # Check if the computer's guess hits any of the player's ships
        if (comp_guess_row, comp_guess_col) in player_ships:
            print("The computer hit your ship!")
            computer_board[comp_guess_row][comp_guess_col] = "X"
            update_sheet(computer_board, 'G')
        else:
            if computer_board[comp_guess_row][comp_guess_col] == "X":
                print("Computer guessed the same spot again!")
            else:
                print("Computer missed!")
                computer_board[comp_guess_row][comp_guess_col] = "X"
                update_sheet(computer_board, 'G')

        # Check if computer sunk all player's ships
        if all_ships_sunk(player_ships, computer_board):
            print("The computer sunk all your ships!")
            break

# Function to display the game rules
def display_rules():
    print("""
    --- Battleships Game Rules ---
    1. Both the player and the computer have 3 ships hidden on a 5x5 grid.
    2. The goal is to sink all of the opponent's ships before they sink yours.
    3. On your turn, enter the row and column you want to attack (0 to 4).
    4. If you hit an opponent's ship, it's marked with 'X' on your guessing board.
    5. The game continues until all ships are sunk.
    """)

# Starting menu
def start_menu():
    while True:
        print("\nWelcome to Battleships!")
        print("1. Read Rules")
        print("2. Start Game")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            display_rules()
        elif choice == "2":
            play_game()
            break
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            sys.exit()
        else:
            print("Invalid input, please enter 1, 2, or 3.")

# Run the menu
if __name__ == '__main__':
    start_menu()
    
