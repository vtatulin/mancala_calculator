import random
from board import Board, MY_FIELD, OP_FIELD

def get_possible_moves(b: Board, field:list):
    ret = []
    for pos in field:
        if b.board[pos] > 0:
            ret.append(pos)
    return ret

def main():
    b = Board()
    print(b)
    move = True
    while not b.game_end:
        if move:

            moves = get_possible_moves(b, MY_FIELD)
            if len(moves) == 0:
                print('Game ends!')
                return
            t = random.choice(moves)
            print(f'my move: {t}')
        else:

            moves = get_possible_moves(b, OP_FIELD)
            if len(moves) == 0:
                print('Game ends!')
                return
            t = random.choice(moves)
            print(f'op move: {t}')

        b.move(t)
        print(b)
        if not b.extra_mowe:
            move = not move
        else:
            print('extra move!!!')



if __name__ == '__main__':
    main()
