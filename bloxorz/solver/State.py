from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Block import Block
from bloxorz.solver.moves import moves


class State():
    def __init__(this, s: Stage):
        # do something to parse the stage to a state
        this.board = s.board
        this.block = Block(s.start_x, s.start_y)
        this.moves = []  # type: List[moves]

    def __repr__(this):
        print(this.moves)

    def isGoal(this):
        return True

    def isValid(this):
        return True

    def up(this):
        print("[*] Move up")

    def down(this):
        print("[*] Move down")

    def left(this):
        print("[*] Move left")

    def right(this):
        print("[*] Move right")
