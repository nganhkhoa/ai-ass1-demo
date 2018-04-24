from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage16():
    B1 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(8)]  # type: List[List[Tile]]

    arr[0] = [None, Tile(T.split, [1,7,1,5])]
    arr[0] += [None for i in range(8)]
    arr[0] += [Tile(), Tile(), Tile()]

    arr[1] = [Tile(T.split, [1,2,0,1]), Tile(), Tile(T.split, [1,0,1,2]), 
                B1[0], B1[1], Tile(T.hard_special_button, B1, []), Tile(T.hard_special_button, B2, []), 
                Tile(), B2[0], B2[1], Tile(), Tile(T.goal), Tile()]

    arr[2] = [None, Tile(T.split, [2,1,1,0])]
    arr[2] += [None for i in range(8)]
    arr[2] += [Tile(), Tile(), Tile()]

    arr[5] = [None, None, Tile(), Tile(), Tile(), None, None, None, Tile(), Tile(), Tile()]

    arr[6] = [None, None]
    arr[6] += [Tile() for i in range(7)]
    arr[6] += [Tile(T.split, [0,1,1,0]), Tile()]

    arr[7] = [None, None, Tile(), Tile(), Tile(), None, None, None, Tile(), Tile(), Tile()]

    s = Stage('stage16', arr, 6, 3)
    s.save('stage16')