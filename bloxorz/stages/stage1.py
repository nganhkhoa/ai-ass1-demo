from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage1():
    arr = [[] for i in range(6)]  # type: List[List[Tile]]

    arr[0] = [Tile(), Tile(), Tile()]

    arr[1] = [Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]

    arr[2] = [Tile(), Tile(), Tile(), Tile(),
              Tile(), Tile(), Tile(), Tile(), Tile()]

    arr[3] = [None, Tile(), Tile(), Tile(), Tile(),
              Tile(), Tile(), Tile(), Tile(), Tile()]

    arr[4] = [None, None, None, None, None,
              Tile(), Tile(), Tile(T.goal), Tile(), Tile()]

    arr[5] = [None, None, None, None, None,
              None, Tile(), Tile(), Tile()]

    s = Stage('1', arr, 1, 1)
    s.save('1')
