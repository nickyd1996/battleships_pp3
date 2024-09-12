def initialize_board():
    return [['O' for _ in range(5)] for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))