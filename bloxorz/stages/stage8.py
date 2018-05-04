from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage8():
    arr = [[] for i in range(9)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(9)]
    arr[0] += [Tile(), Tile(), Tile()]

    arr[1] = [None for i in range(9)]
    arr[1] += [Tile(), Tile(), Tile()]

    arr[2] = [None for i in range(9)]
    arr[2] += [Tile(), Tile(), Tile()]

    arr[3] = [Tile() for i in range(6)]
    arr[3] += [None, None, None]
    arr[3] += [Tile() for i in range(6)]

    arr[4] = [Tile() for i in range(4)]
    arr[4] += [Tile(T.split, [1,10,7,10]), Tile(), None, None, None]
    arr[4] += [Tile(), Tile(), Tile(), Tile(), Tile(T.goal), Tile()]

    arr[5] = [Tile() for i in range(6)]
    arr[5] += [None, None, None]
    arr[5] += [Tile() for i in range(6)]

    arr[6] = [None for i in range(9)]
    arr[6] += [Tile(), Tile(), Tile()]

    arr[7] = [None for i in range(9)]
    arr[7] += [Tile(), Tile(), Tile()]

    arr[8] = [None for i in range(9)]
    arr[8] += [Tile(), Tile(), Tile()]

    s = Stage('8', arr, 4, 1)
    s.save('8')