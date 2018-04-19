from enum import Enum, auto


class moves(Enum):
    right = 4
    left = 3
    up = 1
    down = 2

    def reverse(self):
        if self.value % 2 == 0:
            return moves(self.value - 1)
        else:
            return moves(self.value + 1)

    def isReverse(self, m):
        if self.value % 2 == 0:
            return self.value - 1 == m.value
        else:
            return self.value + 1 == m.value
