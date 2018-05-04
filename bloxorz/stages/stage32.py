from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage32():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B3 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B4 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(9)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(12)]
    arr[0] += [Tile(), Tile(T.hard_button, [B1[0],B1[1],B3[0],B3[1]])]

    arr[1] = [None, None, Tile(), Tile(), B1[0], B1[1], Tile(), Tile(), 
                None, None, None, Tile(), Tile(), Tile()]

    arr[2] = [None, Tile(), Tile(), Tile(), B2[0], B2[1], Tile(), Tile(), 
                None, None, Tile(), Tile(T.hard_button, B4), Tile(), Tile()]

    arr[3] = [None, Tile(), Tile(T.goal), Tile(), None, None, None]
    arr[3] += [Tile() for i in range(5)]

    arr[4] = [None, Tile(), Tile(), Tile()]
    arr[4] += [None for i in range(4)]
    arr[4] += [Tile(), Tile(), Tile()]

    arr[5] = [None for i in range(9)]
    arr[5] += [Tile(), Tile()]

    arr[6] = [None for i in range(4)]
    arr[6] += [Tile(), Tile(), Tile(), None, None, Tile(), Tile()]

    arr[7] = [Tile(), Tile(), B3[0], B3[1], Tile(), Tile(T.hard_button, B2), Tile(), 
                None, None, Tile(), Tile()]

    arr[8] = [Tile(), Tile(), B4[0], B4[1]]
    arr[8] += [Tile() for i in range(7)]

    s = Stage('32', arr, 6, 10)
    s.save('32')