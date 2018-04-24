from enum import Enum, auto


class moves(Enum):
    up = 1
    down = 2
    right = 3
    left = 4
    split = 5
    join = 6
    swap = 7

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

    def normalMove(self):
        if self.value == 7:
            return True
        if self.value > 4:
            return False
        else:
            return True


def print_moves(list_moves, step=None):
    # print the moves
    print("\033[s", end="")      # save cursor
    print("\033[1H", end="")

    frame = []

    i = 0
    start = 1
    for m in list_moves:
        if not m.normalMove() or m == moves.swap:
            continue
        if step is None:
            frame.append(m)
            start += 1
        else:
            if i > step + 3:
                break
            if abs(step - i) <= 3:
                frame.append(m)
            else:
                start += 1

        i += 1

    if step is None:
        frame = frame[-7:]
        start -= len(frame)
        base = len(frame) - 1
    else:
        base = 3

    for i in range(7):
        print("\033[25C", end="")
        if i == base and len(frame) != 0:
            print("\033[31m", end="")
            print("|>  ", end="")
        else:
            if step is None:
                print("|   ", end="")
            elif i < base:
                print("\033[90m", end="")

        try:
            print("{}. ".format(start + i), end="")
            print(frame[i])
        except IndexError:
            print("---")

        print("\033[0m", end="")

    print("\033[0m", end="")
    print("\033[u",end="")      # reload cursor