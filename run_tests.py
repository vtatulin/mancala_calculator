import unittest
import logging

from board import Board

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('tests', )

# logger.setLevel(level=logging.DEBUG)
logger.setLevel(level=logging.INFO)


def positions():
    return [_ for _ in range(14)]


def get_empty_board(b: Board):
    return [0, ] * 14


class TestStringMethods(unittest.TestCase):

    def test_sum(self):
        b = Board()
        s = sum(el for el in b.board)
        self.assertEqual(s, 48)

    def test_initial_score(self):
        b = Board()
        self.assertEqual(b.my_score, 0)
        self.assertEqual(b.op_score, 0)

    def test_mancala_positions(self):
        """
        [  ] [12][11][10][ 9][ 8][ 7] [  ]
        [13]                          [ 6]
        [  ] [ 0][ 1][ 2][ 3][ 4][ 5] [  ]

        """
        b = Board()
        b.board = positions()
        self.assertEqual(b.my_score, 6)
        self.assertEqual(b.op_score, 13)

    def test_my_first_mowe(self):
        b = Board()
        b.move(2)
        logger.info(b)
        self.assertEqual(b.my_score, 1)

    def test_my_capture(self):
        b = Board()
        logger.info(b)
        s = b.move(5)
        logger.info(b)
        s = b.move(1)
        logger.info(b)
        self.assertTrue(b.my_score == 6)
        self.assertTrue(b.op_score == 0)

    def test_ops_capture(self):
        # [ ][0][1][4][4][4][4][ ]
        # [0]                  [0]
        # [ ][4][4][4][4][4][4][ ]
        b = Board()
        b.board[12] = 0
        b.board[11] = 1
        logger.info(b)
        b.move(11)
        self.assertTrue(b.my_score == 0)
        self.assertTrue(b.op_score == 5)

    def test_i_am_not_sowing_ops_mankala(self):
        logger.info("I am not seeding in op's mankala")
        b = Board()
        b.board = get_empty_board(b)
        b.board[5] = 9
        logger.info(b)
        b.move(5)
        logger.info(b)
        self.assertTrue(b.my_score == 3)  # 1 sowed + 2 captured
        self.assertTrue(b.op_score == 0)

    def test_op_is_not_sowing_in_my_mankala(self):
        b = Board()
        b.board = get_empty_board(b)
        b.board[12] = 8
        logger.info(b)
        b.move(12)
        logger.info(b)
        self.assertTrue(b.my_score == 0)
        self.assertTrue(b.op_score == 3)  # 1 sowed + 2 captured

    def test_my_capture(self):
        # [ ][0][0][0][0][0][1][ ]
        # [0]                  [0]
        # [ ][0][0][0][0][1][0][ ]
        b = Board()
        b.board = get_empty_board(b)
        b.board[4] = 1
        b.board[7] = 1
        logger.info(b)
        b.move(4)
        self.assertEqual(2, b.my_score)

    def test_op_capture(self):
        # [ ][0][1][0][0][0][0][ ]
        # [0]                  [0]
        # [ ][10][0][0][0][0][0][ ]
        b = Board()
        b.board = get_empty_board(b)
        b.board[0] = 10
        b.board[11] = 1
        b.move(11)
        self.assertEqual(11, b.op_score)


    def test_my_extra_mowe(self):
        # [][0][0][0][0][0][0][]
        # [0]                [0]
        # [][0][0][0][0][0][1][]
        b = Board()
        b.board = get_empty_board(b)
        b.board[5] = 1
        b.move(5)
        self.assertEqual(True, b.extra_mowe)

    def test_ops_extra_mowe(self):
        b = Board()
        b.board = get_empty_board(b)
        b.board[11] = 2
        b.move(11)
        self.assertEqual(True, b.extra_mowe)

    def test_end_game(self):
        b = Board()
        b.board = get_empty_board(b)
        b.board[13] = 47
        b.board[12] = 1
        b.move(12)
        self.assertEqual(b.game_end, True)

    def test_not_end(self):
        b = Board()
        self.assertEqual(b.game_end, False)
        b.move(5)
        self.assertEqual(b.game_end, False)


if __name__ == '__main__':
    pass
