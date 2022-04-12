from Board.board import Board
from Players.AI import AI
from UI.ui import UI


def start():

    ok = 1
    rows = 0
    cols = 0
    while ok == 1:
        rows = input("Introduce the number of rows for the board: ")
        cols = input("Introduce the number of columns for the board: ")

        if rows > '9' or rows < '0' or cols > '9' or cols < '0':
            print("Not a valid board")
        else:
            ok = 0
            rows = int(rows)
            cols = int(cols)

    ai = AI()
    board = Board(rows, cols)
    ui = UI(board, ai)
    ui.game()


start()
