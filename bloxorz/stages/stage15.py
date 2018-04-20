from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage15():
    B0 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B3 = [Tile(T.bridge, True), Tile(T.bridge, True)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(7)]
    arr[0] += [Tile(), Tile(), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[1] = [None, None, None, None, 
                Tile(), B1[0], B1[1], 
                Tile(), Tile(), Tile(), B2[0], B2[1], 
                Tile(T.hard_button, [B0[0], B0[1], B1[0], B1[1]]), Tile(), Tile()]

    arr[2] = [Tile(), Tile(), B0[0], B0[1], Tile(), 
                None, None, Tile(), Tile(), Tile(), 
                None, None, Tile(), Tile(), Tile()]

    arr[3] = [Tile() for i in range(5)]
    arr[3] += [None, None, None, Tile(T.soft_button, [B1[0], B1[1], B2[0], B2[1]])]

    arr[4] = [Tile(), Tile()]

    arr[5] = [None, Tile()]
    arr[5] += [None for i in range(5)]
    arr[5].append(Tile(T.split, [1,14,8,1]))

    arr[6] = [None, Tile()]
    arr[6] += [None for i in range(5)]
    arr[6].append(Tile())

    arr[7] = [Tile(), Tile(), Tile(), 
                None, None, None, Tile(), Tile(), Tile(), 
                None, None, Tile(T.soft_button, [], B3), Tile(), Tile()]

    arr[8] = [Tile() for i in range(9)]
    arr[8] += [B3[0], B3[1], Tile(), Tile(T.goal), Tile()]

    arr[9] = [Tile(), Tile(), Tile(), 
                None, None, None, Tile(), Tile(), Tile(), 
                None, None, Tile(T.soft_button, [], B3), Tile(), Tile()]

    s = Stage('stage15', arr, 8, 1)
    s.save('stage15')