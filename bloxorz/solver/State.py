from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.solver.moves import moves


class State():
    def __init__(this, s: Stage):
        # do something to parse the stage to a state
        this.board = s.board
        this.block = s.block
        this.moves = []  # type: List[moves]

    def isGoal(this):
        return True
