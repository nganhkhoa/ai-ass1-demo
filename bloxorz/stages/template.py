from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage_():
    arr = [[] for i in range()]  # type: List[List[Tile]]

    s = Stage('stage_', arr, 1, 1)
    s.save('stage_')