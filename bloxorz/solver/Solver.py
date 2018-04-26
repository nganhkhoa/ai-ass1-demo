# from bloxorz.game.Stage import Stage
# from bloxorz.game.Tile import Tile
# from bloxorz.game.Block import Block
# from bloxorz.game.TileType import TileType as T

from typing import List

from bloxorz.solver.State import State
from bloxorz.solver.mode import mode

from bloxorz.solver.BFS import BFS
from bloxorz.solver.DFS import DFS
from bloxorz.solver.HILL import HILL
from bloxorz.solver.ANNEALING import ANNEALING
from bloxorz.solver.BEST import BEST

import queue


class Solver:
    def __init__(self, s: State, m: mode):
        self.queue = queue.Queue()
        self.queue.put(s)
        # self.queue = [s]
        self.mode = m
        self.goal = None
        self.setTrace = set()

    def solve(self):
        if self.mode == mode.bfs:
            print("[+] Solving with bfs now")
            BFS(self)

        elif self.mode == mode.dfs:
            print("[+] Solving with dfs now")
            DFS(self)

        elif self.mode == mode.hill:
            print("[+] Solving with hill climbing now")
            HILL(self)

        elif self.mode == mode.annealing:
            print("[+] Simulated Annealing?")
            ANNEALING(self)

        elif self.mode == mode.best:
            print("[+] Someone says best first?")
            BEST(self)

        else:
            print("[?] LOL what algorithm")

    def __repr__(self):
        if self.goal is not None:
            print("[+] I've found a way:")
            print(self.goal.moves)
            return ""
        else:
            return "--- Sorry, I couldn't do it"
