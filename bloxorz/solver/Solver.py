# from bloxorz.game.Stage import Stage
# from bloxorz.game.Tile import Tile
# from bloxorz.game.Block import Block
# from bloxorz.game.TileType import TileType as T

from typing import List

from bloxorz.solver.State import State
from bloxorz.game.mode import mode

from .BFS import BFS
from .DFS import DFS
from .HILL import HILL
from .ANNEALING import ANNEALING
from .BEST import BEST


class Solver():
    def __init__(this, s: State, m: mode):
        this.queue = [s]
        this.mode = m
        this.goal = None

    def solve(this):
        if this.mode == mode.bfs:
            print("[+] Solving with bfs now")
            BFS(this)

        elif this.mode == mode.dfs:
            print("[+] Solving with dfs now")
            DFS(this)

        elif this.mode == mode.hill:
            print("[+] Solving with hill climbing now")
            HILL(this)

        elif this.mode == mode.annealing:
            print("[+] Simulated Annealing?")
            ANNEALING(this)

        elif this.mode == mode.best:
            print("[+] Someone says best first?")
            BEST(this)

        else:
            print("[?] LOL what algorithm")

    def __repr__(this):
        if this.goal is not None:
            print("[+] I've found a way:")
            return this.goal.moves
        else:
            return "--- Sorry, I couldn't do it"
