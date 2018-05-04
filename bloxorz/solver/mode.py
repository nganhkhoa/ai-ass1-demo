from enum import Enum, auto


class mode(Enum):
    bfs = 1
    dfs = 2
    hill = 3
    annealing = 4
    best = 5

    def __repr__(self):
        return self.name.upper()

    def __str__(self):
        return self.name.upper()
