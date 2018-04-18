from typing import List

from bloxorz.game.Stage import Stage
# from bloxorz.solver.Blox import Blox
from bloxorz.solver.Block import Block
from bloxorz.solver.moves import moves


class State:
    def __init__(self, s: Stage):
        # do something to parse the stage to a state
        self.board = s.board
        self.blox = Block(s.start_x, s.start_y)
        self.moves = []  # type: List[moves]

    def __repr__(this):
        st_blk, nd_blk = this.blox.getIndex()
        i = 0

        # print(st_blk)
        # print(nd_blk)
        # print(this.blox.standing())

        for line in this.board:
            j = 0
            for tile in line:
                if i == st_blk[0] and j == st_blk[1]:
                    print("*", end='')

                elif i == nd_blk[0] and j == nd_blk[1]:
                    print("*", end='')

                elif tile is None:
                    print(" ", end='')

                else:
                    print(tile, end='')
                j += 1
            print()
            i += 1
        return ""

    def isGoal(this):
        if not this.blox.standing():
            return False

        st_blk, nd_blk = this.blox.getIndex()

        return this.board[st_blk[0]][st_blk[1]].isGoal()


    def getAll(self):
        return self.board, self.blox.getIndex(), self.blox.active()

    def getBoard(this):
        return this.board

    def getIndex(this):
        return this.blox.index()

    def isSplit(this):
        return this.blox.isSlipt()

    def getActiveBlock(this):
        return this.blox.active()

    def setActiveBlock(this, b):
        this.blox.setActive(b)

    def move(self, m):
        self.blox.move(m)
        st_blk, nd_blk = self.blox.getIndex()
        standing = self.blox.standing()

        try:
            self.board[st_blk[0]][st_blk[1]].trigger(standing)
            # don't trigger twice
            if not standing:
                self.board[nd_blk[0]][nd_blk[1]].trigger(standing)

        except IndexError:
            self.blox.move(m.reverse())
            raise Exception("IndexError")

        except AttributeError:
            self.blox.move(m.reverse())
            raise Exception("NoneTile")

        except Exception as e:
            self.blox.move(m.reverse())
            raise e

        if self.blox.isSplit():
            # try to join the blocks
            self.blox.join()