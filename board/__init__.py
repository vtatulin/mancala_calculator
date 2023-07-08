"""mancala board class

coordinates:

        [  ] [12][11][10][ 9][ 8][ 7] [  ]
        [13]                          [ 6]
        [  ] [ 0][ 1][ 2][ 3][ 4][ 5] [  ]

initial position:
        [  ] [ 4][ 4][ 4][ 4][ 4][ 4] [  ]
        [ 0]                          [ 0]
        [  ] [ 4][ 4][ 4][ 4][ 4][ 4] [  ]

"""
MY_FIELD = [_ for _ in range(6)]
OP_FIELD = [_ for _ in range(12, 6, -1)]
MY_MANCALA_POS = 6
OP_MANCALA_POS = 13


def filer(pos):
    return ' ' if pos < 10 else ''


def opposing_pos(pos):
    if pos in (MY_MANCALA_POS, OP_MANCALA_POS):
        return None  ## mancala has no opposing position
    return 12 - pos


class Board():
    def __init__(self):
        self.board = [4, ] * 14
        self.board[MY_MANCALA_POS] = 0
        self.board[OP_MANCALA_POS] = 0
        self.stone_sum = sum(self.board)
        ## last mowe capture
        self.captured = 0
        self.extra_mowe = False  ## if mowe ended in mancala
        self.my_mowe = False  ## who mowed stones (seeds) last

    def _get_my_score(self):
        return self.board[MY_MANCALA_POS]

    my_score = property(_get_my_score, None)

    def _get_op_score(self):
        return self.board[OP_MANCALA_POS]

    op_score = property(_get_op_score, None)

    def _get_game_end(self):
        return self.my_score + self.op_score == self.stone_sum

    game_end = property(_get_game_end, None)

    def __repr__(self):
        my_mancala = self.board[MY_MANCALA_POS]
        op_mancala = self.board[OP_MANCALA_POS]
        op_field = ''
        for i in OP_FIELD:
            op_field += f'[{filer(self.board[i])}{self.board[i]}]'
        my_field = ''
        for i in MY_FIELD:
            my_field += f'[{filer(self.board[i])}{self.board[i]}]'

        ret = f"""[  ] {op_field} [  ]
[{filer(op_mancala)}{op_mancala}]                          [{filer(my_mancala)}{my_mancala}]
[  ] {my_field} [  ]
"""
        return ret

    def move(self, pos):
        self.captured = 0
        self.extra_mowe = False
        self.my_mowe = pos in MY_FIELD
        if self.board[pos] == 0:
            raise Exception(f'no stones to take from {pos}')
        if pos == MY_MANCALA_POS:
            raise Exception('do not touch my mankala!')
        if pos == OP_MANCALA_POS:
            raise Exception('do not touch enemy mankala!')

        s = self.sow(pos)
        op_pos = opposing_pos(s)
        # my capture:
        if (self.my_mowe) and (s in MY_FIELD) and (self.board[s] == 1):
            self.captured = self.board[op_pos] + self.board[s]  ## info  field
            self.board[MY_MANCALA_POS] += self.captured
            self.board[op_pos] = 0
            self.board[s] = 0

        ## op's capture:
        if (not self.my_mowe) and (s in OP_FIELD) and (self.board[s] == 1):
            self.captured = self.board[op_pos] + self.board[s]  ## info  field
            self.board[OP_MANCALA_POS] += self.captured
            self.board[op_pos] = 0
            self.board[s] = 0
        if self.my_mowe and (s == MY_MANCALA_POS):
            self.extra_mowe = True
        if (not self.my_mowe) and (s == OP_MANCALA_POS):
            self.extra_mowe = True

        return s

    # def sow(self, i):
    #     ## taking stones from a pit
    #     stones = self.board[i]
    #     self.board[i] = 0
    #     end_pos = i + stones
    #     for pos in range(i + 1, end_pos + 1):
    #         _pos = pos if pos <= 13 else (pos % 13) - 1  ##making round
    #         ## not seeding in op's mankala
    #         if self.my_mowe and _pos == OP_MANCALA_POS:
    #             _pos = 0
    #         ## op is not sowing in my mankala:
    #         if (not self.my_mowe) and _pos == MY_MANCALA_POS:
    #             _pos = 7
    #         self.board[_pos] += 1
    #     return _pos

    def sow(self, i):
        ## taking stones from a pit
        stones = self.board[i]
        self.board[i] = 0
        pos = i
        while stones > 0:
            stones -= 1
            pos += 1
            pos = pos if pos <= 13 else (pos % 13) - 1  ##making round
            ## not seeding in op's mankala
            if self.my_mowe and pos == OP_MANCALA_POS:
                pos = 0
            ## op is not sowing in my mankala:
            if (not self.my_mowe) and pos == MY_MANCALA_POS:
                pos = 7
            self.board[pos] += 1
        return pos


if __name__ == '__main__':
    b = Board()
    print(b)
    t = b.move(2)
    print(b)
    print(f'ended in {t}')

    print('test my capture:')
    b = Board()
    b.move(5)
    print(b)
    b.move(0)
    print(b)
