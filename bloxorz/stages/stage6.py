from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage6():
    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(5)]
    arr[0] += [Tile() for i in range(6)]

    arr[1] = [None for i in range(5)]
    arr[1] += [Tile(), None, None, Tile(), Tile(), Tile()]

    arr[2] = [None for i in range(5)]
    arr[2] += [Tile(), None, None]
    arr[2] += [Tile() for i in range(5)]

    arr[3] = [Tile() for i in range(6)]
    arr[3] += [None for i in range(5)]
    arr[3] += [Tile() for i in range(4)]

    arr[4] = [None for i in range(4)]
    arr[4] += [Tile(), Tile(), Tile()]
    arr[4] += [None for i in range(4)]
    arr[4] += [Tile(), Tile(), Tile(T.goal), Tile()]

    arr[5] = [None for i in range(4)]
    arr[5] += [Tile(), Tile(), Tile()]
    arr[5] += [None for i in range(5)]
    arr[5] += [Tile(), Tile(), Tile()]

    arr[6] = [None for i in range(6)]
    arr[6].append(Tile())
    arr[6] += [None, None, Tile(), Tile()]

    arr[7] = [None for i in range(6)]
    arr[7] += [Tile() for i in range(5)]

    arr[8] = [None for i in range(6)]
    arr[8] += [Tile() for i in range(5)]

    arr[9] = [None for i in range(7)]
    arr[9] += [Tile(), Tile(), Tile()]

    s = Stage('stage6', arr, 3, 0)
    s.save('stage6')