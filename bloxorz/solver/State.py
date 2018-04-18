from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.solver.Blox import Blox
from bloxorz.solver.moves import moves


class State():
    def __init__(this, s: Stage):
        # do something to parse the stage to a state
        this.board = s.board
        this.blox = Blox(s.start_x, s.start_y)
        this.moves = []  # type: List[moves]

    def __repr__(this):
        for line in this.board:
            for tile in line:
                if tile is None:
                    print(" ", end='')
                else:
                    print(tile, end='')
            print()
        return ""

    def isGoal(this):
        return True

    def isValid(this):
        return True

    def move(this, m: moves):
        # you'll only need this:
        # this.blox.move(m)

        # below is for demo only
        if m == moves.left:
            this.left()
        elif m == moves.right:
            this.right()
        elif m == moves.up:
            this.up()
        elif m == moves.down:
            this.down()
        else:
            print("[?] Where the hell should I move")

        # check if this move is valid
        """
        idx = this.blox.index()
        try:
            this.board[idx[0]][idx[1]].trigger()
            this.board[idx[2]][idx[3]].trigger()
        except IndexError:
            raise
        except None:
            raise
        except Fall:
            raise

        # this is a valid move
        """

    def up(this):
        print("[*] Move up")

    def down(this):
        print("[*] Move down")

    def left(this):
        print("[*] Move left")

    def right(this):
        print("[*] Move right")
