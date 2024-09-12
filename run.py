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
