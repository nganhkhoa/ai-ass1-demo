from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage22():
    B1 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(5)]
    arr[0] += [Tile(), Tile(), None, None, None, None, Tile(), Tile(), Tile()]

    arr[1] = [None, None, None]
    arr[1] += [Tile() for i in range(6)]
    arr[1] += [None, None, Tile(), Tile(T.goal), Tile()]

    arr[2] = [Tile() for i in range(6)]
    arr[2] += [Tile(T.soft_button, [], B1)]
    arr[2] += [Tile() for i in range(7)]

    arr[3] = [Tile(), Tile(), Tile(), Tile(), 
                Tile(T.soft_button, [], B1), None, None, 
                Tile(), Tile(), Tile(), Tile(), Tile(), B1[1]]

    arr[4] = [Tile(), Tile(), Tile()]
    arr[4] += [None for i in range(6)]
    arr[4] += [Tile(), Tile(), Tile()]

    arr[5] = [None, Tile()]
    arr[5] += [None for i in range(7)]
    arr[5] += [None, Tile()]

    arr[6] = [None, Tile()]
    arr[6] += [None for i in range(7)]
    arr[6] += [None, Tile()]

    arr[7] = [None, Tile(), B1[0]]
    arr[7] += [None for i in range(6)]
    arr[7] += [Tile(), Tile()]

    arr[8] = [None, Tile(), Tile()]
    arr[8] += [None for i in range(6)]
    arr[8] += [Tile(), Tile()]

    arr[9] = [None, None, Tile(T.hard_button, [B1[1]])]
    arr[9] += [None for i in range(6)]
    arr[9] += [Tile(T.hard_button, [B1[0]])]

    s = Stage('stage22', arr, 3, 1)
    s.save('stage22')