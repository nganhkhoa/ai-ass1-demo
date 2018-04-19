from enum import Enum

from bloxorz.solver.moves import moves


class State(enumerate):
    horizontal = 1
    vertical = 2
    standing = 3
    neutral = 0

class Block:
    splitting = False

    def __init__(self, x, y):
        self.height = 2
        self.state = State.standing
        self.location = [x, y]

    def isSplit(self):
        return self.splitting

    def split(self, places):
        self.location = places
        self.splitting = True
        self.height = 1
        self.state = State.neutral

    def join(self, direction):
        # join to where?
        self.splitting = False
        self.height = 2

        if direction == moves.left or direction == moves.right:
            self.state = State.horizontal
        else:
            self.state = State.vertical

    def setActive(self, blk):
        if self.splitting:
            pass
        else:
            pass

    def standing(self):
        return self.state == State.standing

    def horizon(self):
        return self.state == State.horizontal
    
    def vertical(self):
        return self.state == State.vertical

    def getIndex(self):
        # if self.splitting:
        #     return self.location, self.another

        # second_block = []
        # if self.state == State.standing:
        #     second_block = [self.location[0], self.location[1]]

        # elif self.state == State.horizontal:
        #     second_block = [self.location[0], self.location[1] + 1]

        # elif self.state == State.vertical:
        #     second_block = [self.location[0] + 1, self.location[1]]

        # else:
        #     pass

        return self.location

    def move(self, m: moves):
        if m == moves.left:
            self.move_left()
        elif m == moves.right:
            self.move_right()
        elif m == moves.up:
            self.move_up()
        elif m == moves.down:
            self.move_down()
        else:
            pass

    def move_left_right(self, toLeft):
        if self.state == State.standing:
            delta = -self.height
            if toLeft == -1:
                delta = 1
            self.location[1] += delta
            self.state = State.horizontal

        elif self.state == State.horizontal:
            delta = -1
            if toLeft == -1:
                delta = self.height
            self.location[1] += delta
            self.state = State.standing

        elif self.state == State.vertical:
            self.location[1] -= toLeft
            # unchanged state, still vertical

        else:
            self.location[1] -= toLeft

    def move_up_down(self, toUp):
        if self.state == State.standing:
            delta = -self.height
            if toUp == -1:
                delta = 1
            self.location[0] += delta
            self.state = State.vertical

        elif self.state == State.horizontal:
            self.location[0] -= toUp

        elif self.state == State.vertical:
            delta = 1
            if toUp == -1:
                delta = -self.height
            self.location[0] -= delta
            self.state = State.standing

        else:
            self.location[0] -= toUp

    def move_left(self):
        self.move_left_right(1)

    def move_right(self):
        self.move_left_right(-1)

    def move_up(self):
        self.move_up_down(1)

    def move_down(self):
        self.move_up_down(-1)

    """
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
    """