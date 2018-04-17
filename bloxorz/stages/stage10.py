from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage10():
    arr = [[] for i in range(0)]  # type: List[List[Tile]]

    s = Stage('stage10', arr, 1, 1)
    s.save('stage10')