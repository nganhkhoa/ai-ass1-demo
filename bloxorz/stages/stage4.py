from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage4():
    arr = [[] for i in range(9)]

    arr[0] = [None, None, None] + [Tile(T.soft_ground) for i in range(7)]

    arr[1] = [None, None, None] + [Tile(T.soft_ground) for i in range(7)]

    arr[2] = [Tile() for i in range(4)] + [None for i in range(5)]
    arr[2] += [Tile() for i in range(3)]

    arr[3] = [Tile(), Tile(), Tile()] + [None for i in range(7)]
    arr[3] += [Tile(), Tile()]

    arr[4] = [Tile(), Tile(), Tile()] + [None for i in range(7)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), None, None]
    arr[5] += [Tile() for i in range(4)]
    arr[5] += [Tile(T.soft_ground) for i in range(5)]

    arr[6] = [Tile(), Tile(), Tile(), None, None]
    arr[6] += [Tile() for i in range(4)]
    arr[6] += [Tile(T.soft_ground) for i in range(5)]

    arr[7] = [None for i in range(5)]
    arr[7] += [Tile(), Tile(T.goal), Tile(), None, None,
               Tile(T.soft_ground), Tile(T.soft_ground),
               Tile(), Tile(T.soft_ground)]

    arr[8] = [None for i in range(5)] + [Tile(), Tile(), Tile(), None, None]
    arr[8] += [Tile(T.soft_ground) for i in range(4)]

    s = Stage('4', arr, 5, 1)
    s.save('4')
