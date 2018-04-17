# from bloxorz.game.Stage import Stage
# from bloxorz.game.Tile import Tile
# from bloxorz.game.Block import Block
# from bloxorz.game.TileType import TileType as T

from bloxorz.solver.State import State
from .BFS import BFS
from .DFS import DFS
from .HILL import HILL
from .ANNEALING import ANNEALING
from .FIRST import FIRST


def bfs(s):
    BFS()


def dfs(s):
    DFS()


def hill(s):
    HILL()


def annealing(s):
    ANNEALING()


def first(s):
    FIRST()
