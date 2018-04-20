from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage32():
    arr = [[] for i in range(9)]  # type: List[List[Tile]]

    arr[0] = []

    s = Stage('stage32', arr, 6, 10)
    s.save('stage32')