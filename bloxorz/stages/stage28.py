from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage28():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, True), Tile(T.bridge, True)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None, Tile(), Tile(), B1[0], B1[1], Tile(), Tile()]

    arr[1] = [None, Tile(), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[2] = [Tile(T.soft_ground), Tile(T.soft_ground), Tile(), 
                None, None, Tile(), Tile(), Tile(), Tile()]

    arr[3] = [Tile(T.soft_ground), Tile(T.soft_ground)]
    arr[3] += [None for i in range(5)]
    arr[3] += [Tile(), Tile(), Tile()]

    arr[4] = [Tile(T.soft_ground), Tile(T.soft_ground)]
    arr[4] += [None for i in range(6)]
    arr[4] += [Tile(), Tile(), Tile()]

    arr[5] = [Tile(T.soft_ground), Tile(), Tile(), Tile()]
    arr[5] += [None for i in range(5)]
    arr[5] += [Tile(), Tile(), Tile(T.split, [6,14,9,12])]

    arr[6] = [None, Tile(), Tile(T.goal), Tile()]
    arr[6] += [None for i in range(6)]
    arr[6] += [Tile() for i in range(5)]

    arr[7] = [None]
    arr[7] += [Tile() for i in range(6)]
    arr[7] += [None, None, None, Tile(), Tile(T.soft_special_button, [], [B1[0], B1[1], B2[0], B2[1]]), 
                Tile(), Tile(), Tile()]

    arr[8] = [None, None, Tile(), None, None, 
                Tile(), Tile(), None, None, None, Tile(), Tile(), Tile()]

    arr[9] = [None, None, Tile(), None, None, 
                Tile(), Tile(), Tile(), B2[0], B2[1], Tile(), Tile(), Tile()]

    s = Stage('stage28', arr, 2, 2)
    s.save('stage28')