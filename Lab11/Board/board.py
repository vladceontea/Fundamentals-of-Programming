from texttable import Texttable


class Board:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._board = self.create_board()

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def create_board(self):
        """
        Creates the board for the new game
        :return: The newly created board
        """
        board = []
        for i in range(self._rows):
            board_rows = []
            for j in range(self._cols):
                board_rows.append(' ')
            board.append(board_rows)
        return board

    def move(self, row, col, value):
        """
        Puts the move on the board and surrounds it with 'x'
        :param row: The row of the cell chosen
        :param col: The col of the cell chosen
        :param value: The symbol of the player doing the move
        :return: -
        """

        self._board[row][col] = value

        if row == 0 and col == 0:
            self._board[row][col+1] = 'x'
            self._board[row+1][col+1] = 'x'
            self._board[row+1][col] = 'x'
        elif row == 0 and col == self._cols - 1:
            self._board[row][col-1] = 'x'
            self._board[row+1][col-1] = 'x'
            self._board[row+1][col] = 'x'
        elif row == 0 and col != 0 and col != self._cols - 1:
            self._board[row][col + 1] = 'x'
            self._board[row + 1][col + 1] = 'x'
            self._board[row + 1][col] = 'x'
            self._board[row][col-1] = 'x'
            self._board[row+1][col-1] = 'x'

        if row == self._rows - 1 and col == 0:
            self._board[row][col+1] = 'x'
            self._board[row-1][col + 1] = 'x'
            self._board[row-1][col] = 'x'
        elif row == self._rows - 1 and col == self._cols - 1:
            self._board[row][col-1] = 'x'
            self._board[row-1][col-1] = 'x'
            self._board[row-1][col] = 'x'
        elif row == self._rows - 1 and col != 0 and col != self._cols - 1:
            self._board[row][col+1] = 'x'
            self._board[row-1][col + 1] = 'x'
            self._board[row-1][col] = 'x'
            self._board[row][col-1] = 'x'
            self._board[row-1][col-1] = 'x'

        if col == 0 and row != 0 and row != self._rows - 1:
            self._board[row-1][col] = 'x'
            self._board[row-1][col+1] = 'x'
            self._board[row][col+1] = 'x'
            self._board[row+1][col] = 'x'
            self._board[row+1][col+1] = 'x'

        if col == self._cols - 1 and row != 0 and row != self._rows - 1:
            self._board[row-1][col] = 'x'
            self._board[row-1][col-1] = 'x'
            self._board[row][col-1] = 'x'
            self._board[row+1][col] = 'x'
            self._board[row+1][col-1] = 'x'

        if row != 0 and row != self._rows - 1 and col != 0 and col != self._cols - 1:
            self._board[row-1][col-1] = 'x'
            self._board[row-1][col] = 'x'
            self._board[row-1][col+1] = 'x'
            self._board[row][col-1] = 'x'
            self._board[row][col+1] = 'x'
            self._board[row+1][col-1] = 'x'
            self._board[row+1][col] = 'x'
            self._board[row+1][col+1] = 'x'

    def check_move(self, row, col):
        """
        Checks if the cell chosen is empty
        :param row: The row of the cell chosen
        :param col: The col of the cell chosen
        :return: True if the move is valid, False otherwise
        """

        if self._board[row][col] == ' ':
            return True
        else:
            return False

    def empty_cells(self):
        """
        Computes the number of empty cells left on the board
        :return: The number of empty cells
        """
        k = 0
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == ' ':
                    k = k + 1
        return k

    def list_empty_cells(self):
        """
        Creates a list of the empty cells on the board
        :return: The list of empty cells
        """
        empty_cells = []
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == ' ':
                    empty = [row, col]
                    empty_cells.append(empty)
        return empty_cells

    def empty_around(self, row, col):
        """
        Computes the number of empty spaces around a certain cell
        :param row: The row of the cell chosen
        :param col: The col of the cell chosen
        :return: The number of empty neighbouring spaces
        """

        empty_neighbours = 0
        if row == 0 and col == 0:
            if self._board[row][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
        elif row == 0 and col == self._cols - 1:
            if self._board[row][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
        elif row == 0 and col != 0 and col != self._cols - 1:
            if self._board[row][col + 1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row + 1][col + 1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row + 1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1

        if row == self._rows - 1 and col == 0:
            if self._board[row][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col + 1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
        elif row == self._rows - 1 and col == self._cols - 1:
            if self._board[row][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
        elif row == self._rows - 1 and col != 0 and col != self._cols - 1:
            if self._board[row][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col + 1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1

        if col == 0 and row != 0 and row != self._rows - 1:
            if self._board[row-1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1

        if col == self._cols - 1 and row != 0 and row != self._rows - 1:
            if self._board[row-1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1

        if row != 0 and row != self._rows - 1 and col != 0 and col != self._cols - 1:
            if self._board[row-1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row-1][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col-1] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col] == ' ':
                empty_neighbours = empty_neighbours + 1
            if self._board[row+1][col+1] == ' ':
                empty_neighbours = empty_neighbours + 1

        return empty_neighbours

    def __str__(self):
        """
        The visible representation of the board
        :return: The board as it is viewed by the player
        """
        t = Texttable()
        board = []
        for row in range(self._rows):
            board.append(self._board[row])
            for col in range(self._cols):
                board[row][col] = self._board[row][col]
        for row in board:
            t.add_row(row)
        return t.draw()
