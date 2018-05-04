from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage11():
    B = [Tile(T.bridge, True), Tile(T.bridge, True)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None, Tile(), Tile(), Tile(), B[0]]

    arr[1] = [None, Tile(), Tile(T.goal), Tile(), B[1]]

    arr[2] = [None, Tile(), Tile(), Tile()]

    arr[3] = [None, Tile(), None, None, None]
    arr[3] += [Tile() for i in range(6)]

    arr[4] = [None, Tile(), None, None, None]
    arr[4] += [Tile(), Tile(), None, None, Tile(), Tile()]

    arr[5] = [Tile() for i in range(7)]
    arr[5] += [None, None, Tile(), Tile(), Tile()]

    arr[6] = [None for i in range(5)]
    arr[6] += [Tile(), Tile(T.soft_special_button, [], B)]
    arr[6] += [None for i in range(4)]
    arr[6] += [Tile()]

    arr[7] = [None for i in range(5)]
    arr[7] += [Tile() for i in range(4)]
    arr[7] += [None, None, Tile()]

    arr[8] = [None for i in range(5)]
    arr[8] += [Tile() for i in range(7)]

    arr[9] = [None for i in range(8)]
    arr[9] += [Tile(), Tile(), Tile()]

    s = Stage('11', arr, 5, 0)
    s.save('11')