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
        print()

    def isGoal(this):
        return True

    def isValid(this):
        return True

    def move(this, m: moves):
        if m == moves.left:
            this.left()
        elif m == moves.right:
            this.right()
        elif m == moves.up:
            this.up()
        elif m == moves.down:
            this.down()
        else:
            print("[?] Where the hell shoul I move")

    def up(this):
        print("[*] Move up")

    def down(this):
        print("[*] Move down")

    def left(this):
        print("[*] Move left")

    def right(this):
        print("[*] Move right")
