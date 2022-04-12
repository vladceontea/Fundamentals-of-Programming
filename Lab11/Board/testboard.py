import unittest

from Board.board import Board


class TestBoard(unittest.TestCase):

    def test_create_board(self):
        board = Board(5, 7)

        self.assertEqual(len(board._board[0]), 7)
        self.assertEqual(len(board._board), 5)

    def test_move(self):
        board = Board(5, 7)
        board.move(2, 5, '*')

        self.assertEqual(board._board[2][5], '*')
        self.assertEqual(board._board[1][4], 'x')
        self.assertEqual(board._board[1][5], 'x')
        self.assertEqual(board._board[1][6], 'x')
        self.assertEqual(board._board[2][4], 'x')
        self.assertEqual(board._board[2][6], 'x')
        self.assertEqual(board._board[3][4], 'x')
        self.assertEqual(board._board[3][5], 'x')
        self.assertEqual(board._board[3][6], 'x')

    def test_check_move(self):
        board = Board(5, 7)
        board.move(2, 5, '*')

        self.assertEqual(board.check_move(0, 0), True)
        self.assertEqual(board.check_move(2, 4), False)

    def test_empty_cells(self):
        board = Board(5, 7)
        board.move(2, 5, '*')

        k = board.empty_cells()
        self.assertEqual(k, 26)

    def test_list_empty_cells(self):
        board = Board(5, 7)
        board.move(2, 5, '*')

        k = board.list_empty_cells()
        self.assertEqual(len(k), 26)

    def test_empty_around(self):
        board = Board(5, 7)
        board.move(2, 5, '*')

        k = board.empty_around(0, 0)
        self.assertEqual(k, 3)
