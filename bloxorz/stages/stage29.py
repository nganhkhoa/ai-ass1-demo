from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage29():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B3 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B4 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B5 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B6 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B7 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B8 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    SB = Tile(T.bridge, False)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None, None, Tile(T.soft_special_button, B2, B5), B1[0], B1[1], Tile(), 
                None, None, None, Tile(), B2[0], B2[1], Tile(T.hard_special_button, B4, [])]

    arr[1] = [None for i in range(5)]
    arr[1] += [Tile(), None, None, None, Tile()]

    arr[2] = [None for i in range(5)]
    arr[2] += [Tile() for i in range(5)]

    arr[3] = [Tile(T.hard_special_button, B7, B8), B6[0], B6[1]]
    arr[3] += [Tile() for i in range(9)]
    arr[3] += [B3[0], B3[1], Tile(T.hard_special_button, [SB], [])]

    arr[4] = [None for i in range(5)]
    arr[4] += [Tile() for i in range(5)]

    arr[5] = [None for i in range(5)]
    arr[5] += [B4[0], Tile(), None, None, Tile()]

    arr[6] = [None for i in range(5)]
    arr[6] += [B4[1], Tile(), None, None, Tile(), B5[0], B5[1], Tile(T.soft_special_button, B6, [])]

    arr[7] = [Tile(), Tile(), Tile(), None, None, Tile(), Tile(), None, None, Tile()]

    arr[8] = [Tile(), Tile(T.goal), Tile(), B7[0], B7[1], Tile(), None, None, None, Tile()]

    arr[9] = [Tile(), Tile(), Tile(), SB]
    arr[9] += [None for i in range(5)]
    arr[9] += [Tile(), B8[0], B8[1], 
                Tile(T.soft_special_button, [B3[0],B3[1]], [B1[0],B1[1],B2[0],B2[1],B5[0],B5[1]])]

    s = Stage('stage29', arr, 3, 7)
    s.save('stage29')