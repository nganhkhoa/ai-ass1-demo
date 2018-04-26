from enum import Enum, auto


class moves(Enum):
    notmove = 0
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
    print("\033[s")      # save cursor
    print("\033[1H", end="")

    frame = []

    i = 0
    start = 1
    list_moves = [m for m in list_moves if m.normalMove()]

    if step is None:
        if len(list_moves) <= 7:
            frame = ["---" for i in range(7 - len(list_moves))] + list_moves
        else:
            frame = list_moves[-7:]
        base = 6
    else:
        if len(list_moves) <= 7 or step <= 3:
            frame = list_moves[step:step + 4]
            frame = ["---" for i in range(3)] + frame
            for i in range(3):
                if step - 3 + i >= 0:
                    frame[i] = list_moves[step - 3 + i]
        else:
            frame = list_moves[step - 3:]
            if len(frame) > 7:
                frame = frame[:7]
        base = 3
        step += 1
        start = step - 3

    for i in range(7):
        print("\033[25C", end="")
        if i == base and len(frame) != 0:
            print("\033[91m", end="")
            print("|>  ", end="")
            if step is not None:
                print("{}. ".format(step), end="")
            else:
                print("{}. ".format(start + i), end="")
        else:
            print("|   ", end="")
            if step is None:
                print("{}. ".format(start + i), end="")
            else:
                if i < base:
                    print("\033[90m", end="")
                print("{}. ".format(start + i if start + i >= 0 else 0), end="")

        try:
            print(frame[i])
        except IndexError:
            print("---")
        except AttributeError:
            print("---")

        print("\033[0m", end="")

    print("\033[0m", end="")
    print("\033[u")      # reload cursor