from enum import Enum


class State(enumerate):
    horizontal = 1
    vertical = 2
    standing = 3

class Block:
    blocks = []
    numberBlocks = len(blocks)
    slipt = False

    def __init__(self, x, y):
        self.height = 2
        self.state = State.standing
        self.location = [x, y]
        Block.blocks.append(self)

    def isSlipt(self):
        return self.slipt

    def getIndex(self):
        return self.location

    def move_left_right(self, matrix, factor):
        if self.state == State.standing:
            delta = -1*self.height
            if factor == -1:
                delta = 1
            for i in range(1, self.height + 1):
                if not matrix[self.location[0]][self.location[1] - i*factor].trigger(False):
                    return False
            self.location = [self.location[0], self.location[1] + delta]
            self.state = State.horizontal
            return True
        elif self.state == State.horizontal:
            delta = -1
            if factor == -1:
                delta = self.height
            if not matrix[self.location[0]][self.location[1] + delta].trigger(True):
                return False
            self.location = [self.location[0], self.location[1] + delta]
            self.state = State.standing
            return True
        elif self.state == State.vertical:
            for i in range(self.height):
                if not matrix[self.location[0] - i][self.location[1] - 1*factor].trigger(False):
                    return False
            self.location = [self.location[0], self.location[1] - 1*factor]
            return True
            # unchanged state, still vertical

    def move_up_down(self, matrix, factor):
        if self.state == State.standing:
            delta = -1*self.height
            if factor == -1:
                delta = 1
            for i in range(1, self.height + 1):
                if not matrix[self.location[0] - i*factor][self.location[1]].trigger(False):
                    return False
            self.location = [self.location[0] + delta][self.location[1]]
            self.state = State.vertical
        elif self.state == State.horizontal:
            for i in range(self.height):
                if not matrix[self.location[0] - 1*factor][self.location[1] + i].trigger(False):
                    return False
            self.location[0] = self.location[0] - 1*factor
            return True
            # unchanged state, still horizontal
        elif self.state == State.vertical:
            delta = 1
            if factor == -1:
                delta = -1*self.height
            if matrix[self.location[0] - delta][self.location[1]].trigger(False):
            for i in range(self.height):
                matrix[self.location[0] + i][self.location[1]] = 0
            self.location[0] = self.location[0] - delta
            self.state = State.standing

    def move_left(self, matrix):
        return self.move_left_right(matrix, 1)

    def move_right(self, matrix):
        return self.move_left_right(matrix, -1)

    def move_up(self, matrix):
        return self.move_up_down(matrix, 1)

    def move_down(self, matrix):
        return self.move_up_down(matrix, -1)

    def can_move_left_right(self, matrix, factor):
        if self.state == State.standing:
            for i in range(1, self.height + 1):
                d = self.location[1] - i * factor
                if d < 0 or d >= len(matrix[self.location[0]]):
                    return False
            return True
        elif self.state == State.horizontal:
            delta = -1
            if factor == -1:
                delta = self.height
            d = self.location[1] + delta
            if d < 0 or d >= len(matrix[self.location[0]]):
                return False
            return True
        elif self.state == State.vertical:
            for i in range(self.height):
                r = self.location[0] - i
                c = self.location[1] - 1 * factor
                if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[r]):
                    return False
            return True

    def can_move_up_down(self, matrix, factor):
        if self.state == State.standing:
            for i in range(1, self.height + 1):
                d = self.location[0] - i*factor
                if d < 0 or d >= len(matrix):
                    return False
            return True
        elif self.state == State.horizontal:
            for i in range(self.height):
                r = self.location[0] - 1*factor
                c = self.location[1] + i
                if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[r]):
                    return False
            return True
        elif self.state == State.vertical:
            delta = 1
            if factor == -1:
                delta = -1*self.height
            d = self.location[0] - delta
            if d < 0 or d >= len(matrix):
                return False
            return True

    def can_move_left(self,matrix):
        return self.can_move_left_right(matrix, 1)

    def can_move_right(self, matrix):
        return self.can_move_left_right(matrix, -1)

    def can_move_up(self, matrix):
        return self.can_move_up_down(matrix, 1)

    def can_move_down(self, matrix):
        return self.can_move_up_down(matrix, -1)

