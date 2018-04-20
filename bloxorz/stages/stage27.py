from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage27():
    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = []

    s = Stage('stage27', arr, 1, 1)
    s.save('stage27')