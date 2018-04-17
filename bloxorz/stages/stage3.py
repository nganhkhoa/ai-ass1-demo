from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage3():
    arr = [[] for i in range(6)]

    arr[0] = [None for i in range(6)]
    arr[0] += [Tile() for i in range(7)]

    arr[1] = [Tile() for i in range(4)] + [None, None]
    arr[1] += [Tile() for i in range(3)] + [None, None, Tile(), Tile()]

    arr[2] = [Tile() for i in range(9)] + [None, None]
    arr[2] += [Tile() for i in range(4)]

    arr[3] = [Tile() for i in range(4)] + [None for i in range(7)]
    arr[3] += [Tile(), Tile(), Tile(T.goal), Tile()]

    arr[4] = [Tile() for i in range(4)] + [None for i in range(7)]
    arr[4] += [Tile(), Tile(), Tile(), Tile()]

    arr[5] = [None for i in range(12)] + [Tile(), Tile(), Tile()]

    s = Stage('stage3', arr, 1, 3)
    s.save('stage3')
