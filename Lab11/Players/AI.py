import random


class AI:

    @staticmethod
    def move(board):
        """
        Creates a move by the computer (will choose the cell with the most empty neighbouring cells)
        :param board: The state of the board when the computer is making the move
        :return: -
        """
        max_len = -1
        row_move = -1
        col_move = -1
        empty_cells = board.list_empty_cells()
        for index in range(len(empty_cells)):
            row = empty_cells[index][0]
            col = empty_cells[index][1]
            empty_neighbours = board.empty_around(row, col)
            if empty_neighbours > max_len:
                max_len = empty_neighbours
                row_move = row
                col_move = col
        board.move(row_move, col_move, 'O')

    @staticmethod
    def random_move(board):
        """
        Createa the first move by the computer, which is random
        :param board: The state of the board when the computer is making the move
        :return: -
        """
        ok = 1
        while ok == 1:
            row = random.randint(0, board.rows-1)
            col = random.randint(0, board.cols-1)

            if board.check_move(row, col):
                board.move(row, col, 'O')
                ok = 0

