from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.solver.Blox import Blox
from bloxorz.solver.moves import moves


class State:
    def __init__(self, s: Stage):
        # do something to parse the stage to a state
        self.board = s.board
        self.Block = Block(s.start_x, s.start_y)
        self.moves = []  # type: List[moves]

    def __repr__(self):
        for line in this.board:
            for tile in line:
                if tile is None:
                    print(" ", end='')
                else:
                    print(tile, end='')
            print()
        return ""

    def getAll(self):
        return self.board, self.block.getIndex(), self.block.active()

    def getBoard(this):
        return this.board

    def getIndex(this):
        return this.blox.index()

    def isSplit(this):
        return this.blox.splitting()

    def getActiveBlock(this):
        return this.blox.active()

    def setActiveBlock(this, b):
        this.blox.setActive(b)