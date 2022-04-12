
class UI:

    def __init__(self, board, ai):
        self._ai = ai
        self._board = board

    def game(self):
        k = '0'
        p = 2
        while k == '0':
            k = input("Would you like to start? (Yes/No)")
            if k == "Yes":
                p = 1
            elif k == "No":
                p = 0
            else:
                "Not a valid answer!"
                k = "0"

        comp = 0
        while True:
            if p == 1:
                ok = 1
                print(str(self._board))
                while ok == 1:
                    row = input("Enter the row (starting from 1): ")
                    col = input("Enter the column (starting from 1): ")
                    if row > '9' or row < '0' or col > '9' or col < '0':
                        print("Not a valid move")
                    else:
                        row = int(row)
                        col = int(col)
                        row = row - 1
                        col = col - 1
                        if 0 <= col < self._board.cols and 0 <= row < self._board.rows:
                            if not self._board.check_move(row, col):
                                print("Not a valid move")
                            else:
                                self._board.move(row, col, 'S')
                                ok = 0
                        else:
                            print("Not a valid move")
                if self._board.empty_cells() == 0:
                    print(str(self._board))
                    print("The player has won!")
                    return
                else:
                    p = 0

            if p == 0:
                if comp == 0:
                    self._ai.random_move(self._board)
                    comp = 1
                else:
                    self._ai.move(self._board)

                if self._board.empty_cells() == 0:
                    print(str(self._board))
                    print("The computer has won!")
                    return
                else:
                    p = 1
