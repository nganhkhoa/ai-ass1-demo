from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.solver.Block import Block
from bloxorz.common.moves import moves


def getIdx(blox):
    idx1 = blox[0].getIndex()
    idx2 = [idx1[0], idx1[1]]

    if blox[1] == None:
        if blox[0].horizon():
            idx2[1] += 1
        elif blox[0].vertical():
            idx2[0] += 1
        else:
            pass
    else:
        # is spliting
        idx2 = blox[1].getIndex()

    return idx1, idx2


def move(self, m):
    block = self.blox[self.selection - 1]

    block.move(m)

    idx1, idx2 = getIdx(self.blox)
    if self.selection == 2:
        # turn bold mode for idx2
        # thus swap them
        idx1, idx2 = idx2, idx1

    if idx1[0] < 0 or idx1[1] < 0 or \
       idx2[0] < 0 or idx2[1] < 0:
        block.move(m.reverse())
        raise Exception("IndexError")

    standing = block.standing()
    splitting = block.isSplit()

    try:
        ret = self.board[idx1[0]][idx1[1]].trigger(standing)
        # don't trigger twice
        if not standing and not splitting:
            self.board[idx2[0]][idx2[1]].trigger(standing)
        else:
            # if standing --> already triggered
            # if splitting --> the remaining block is not move
            pass

    except IndexError:
        self.blox[0].move(m.reverse())
        raise Exception("IndexError")

    except AttributeError:
        self.blox[0].move(m.reverse())
        raise Exception("NoneTile")

    except Exception as e:
        self.blox[0].move(m.reverse())
        raise e

    if ret is not None:
        # hit a split button
        self.blox[0].split(ret[0:2])
        self.blox[1] = Block(ret[2], ret[3])
        self.blox[1].height = 1

    # try to join blocks
    self.join()

    # record the moves
    self.moves.append(m)


class State:
    def __init__(self, s: Stage):
        # do something to parse the stage to a state
        self.board = s.board
        self.blox = [Block(s.start_x, s.start_y), None]
        self.selection = 1
        self.start = [s.start_x, s.start_y]
        self.moves = []  # type: List[moves]

    def __repr__(self):
        idx1, idx2 = getIdx(self.blox)
        if self.selection == 2:
            # turn bold mode for idx2
            # thus swap them
            idx1, idx2 = idx2, idx1
        i = 0

        # print(idx1)
        # print(idx2)
        # print(self.blox[0].state)

        for line in self.board:
            j = 0
            for tile in line:
                if i == idx1[0] and j == idx1[1]:
                    print("\033[1;91m*\033[0m", end='')

                elif i == idx2[0] and j == idx2[1]:
                    print("*", end='')

                elif tile is None:
                    print(" ", end='')

                else:
                    print(tile, end='')
                j += 1
            print()
            i += 1
        return ""

    def isGoal(self):
        if not self.blox[0].standing():
            return False

        st_blk = self.blox[0].getIndex()

        return self.board[st_blk[0]][st_blk[1]].isGoal()

    def isBegin(self):
        if not self.blox[0].standing():
            return False

        st_blk = self.blox[0].getIndex()

        return st_blk[0] == self.start[0] and st_blk[1] == self.start[1]


    def getAll(self):
        return self.board, self.blox[0].getIndex(), self.blox[0].active()

    def getBoard(self):
        return self.board

    def getIndex(self):
        return self.blox[0].index()

    def isSplit(self):
        return self.blox[0].isSplit()

    def getActiveBlock(self):
        return self.blox[self.selection - 1].getIndex()

    def setActiveBlock(self, b):
        self.selection = b

    def toggleActive(self):
        self.selection = 2 if self.selection == 1 else 1

    def join(self):
        if not self.isSplit():
            return

        idx1, idx2 = getIdx(self.blox)

        if idx1[0] == idx2[0]:
            if abs(idx1[1] - idx2[1]) == 1:
                if idx1[1] > idx2[1]:
                    self.blox[0].join(moves.left)
                    self.blox[0].location[1] -= 1
                else:
                    self.blox[0].join(moves.right)
                self.blox[1] = None
                self.selection = 1
                return

        if idx1[1] == idx2[1]:
            if abs(idx1[0] - idx2[0]) == 1:
                if idx1[0] > idx2[0]:
                    self.blox[0].join(moves.up)
                    self.blox[0].location[0] -= 1
                else:
                    self.blox[0].join(moves.down)
                self.blox[1] = None
                self.selection = 1
                return