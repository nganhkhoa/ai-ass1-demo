from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage25():
    B1 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B2 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B3 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB1 = Tile(T.bridge, False)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None, None, Tile(), Tile()]

    arr[1] = [None, None, Tile(), Tile(), Tile()]

    arr[2] = [None, None, Tile(), Tile(), Tile(T.soft_button, [B1[0], B1[1], B3[0], B3[1]])]
    arr[2] += [None for i in range(5)]
    arr[2] += [Tile(), Tile(), Tile()]

    arr[3] = [None, None, None, Tile(), Tile(), Tile(), Tile(), 
                SB1, None, None, Tile(), Tile(T.goal), Tile()]

    arr[4] = [None for i in range(6)]
    arr[4] += [Tile(), Tile(), B1[0], B1[1], Tile(), Tile(), Tile()]

    arr[5] = [None, Tile(), Tile(), None, None, None, Tile(), Tile()]

    arr[6] = [Tile(), Tile(), Tile(T.hard_button, B1, []), Tile(), B2[0], B2[1], Tile(), Tile()]

    arr[7] = [Tile(), Tile(), Tile(), None, None, None, Tile(), Tile()]

    arr[8] = [Tile(), Tile(), Tile(), None, None, None, Tile(), Tile(), Tile(T.soft_button, [SB1], B2)]
    arr[8] += [Tile() for i in range(5)]

    arr[9] = [None for i in range(11)]
    arr[9] += [Tile(), Tile(), Tile()]

    s = Stage('stage25', arr, 7, 1)
    s.save('stage25')