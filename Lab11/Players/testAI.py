import unittest

from Board.board import Board
from Players.AI import AI


class TestAI(unittest.TestCase):
    def test_move(self):
        ai = AI()
        board = Board(6, 6)
        ai.move(board)
        ai.move(board)
        k = 0
        for row in range(board.rows):
            for col in range(board.cols):
                if board._board[row][col] == 'O':
                    k = k + 1
        self.assertEqual(k, 2)
        self.assertEqual(board._board[1][1], 'O')

    def test_random_move(self):
        ai = AI()
        board = Board(6, 6)
        ai.random_move(board)
        k = 0
        for row in range(board.rows):
            for col in range(board.cols):
                if board._board[row][col] == 'O':
                    k = k + 1
        self.assertEqual(k, 1)
