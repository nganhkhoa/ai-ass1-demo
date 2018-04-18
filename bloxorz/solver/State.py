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
        idx = this.blox.index()
        standing = this.blox.standing()
        try:
            return this.board[idx[0]][idx[1]].isGoal() and standing
        except:
            return False

    def getAll(this):
        return this.board, this.blox.index(), this.blox.active()

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

    def move(this, m: moves):
        # DEMO ONLY
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

        # REAL WORK
        """
        this.blox.move(m)
        idx = this.blox.index()
        standing = this.blox.standing()
        try:
            this.board[idx[0]][idx[1]].trigger(standing)
            this.board[idx[2]][idx[3]].trigger(standing)
        except IndexError:
            raise
        except None:
            raise
        except Fall:
            raise
        # except Split:
        #   ...

        # this is a valid move
        if this.blox.spliting():
            this.blox.join()
        """

    def up(this):
        print("[*] Move up")

    def down(this):
        print("[*] Move down")

    def left(this):
        print("[*] Move left")

    def right(this):
        print("[*] Move right")
