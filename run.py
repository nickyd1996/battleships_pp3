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

#initialize the board
def initialize_board():
    return [['O' for _ in range(5)] for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))
