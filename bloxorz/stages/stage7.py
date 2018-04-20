from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage7():
    B = [Tile(T.bridge, False)]

    arr = [[] for i in range(8)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(8)]
    arr[0] += [Tile() for i in range(4)]

    arr[1] = [None for i in range(8)]
    arr[1] += [Tile() for i in range(4)]

    arr[2] = [Tile(), Tile(), Tile()]
    arr[2] += [None for i in range(5)]
    arr[2] += [Tile(), None, None]
    arr[2] += [Tile() for i in range(4)]

    arr[3] = [Tile() for i in range(9)]
    arr[3] += [None, None, None, Tile(), Tile(T.goal), Tile()]

    arr[4] = [Tile(), Tile(), Tile()]
    arr[4] += [None for i in range(4)]
    arr[4] += [Tile(), Tile(), Tile(T.hard_button, B), 
                None, None, Tile(), Tile(), Tile()]
        
    arr[5] = [Tile(), Tile(), Tile()]
    arr[5] += [None for i in range(4)]
    arr[5] += [Tile(), Tile(), Tile(), 
                None, None, Tile(), Tile(), Tile()]

    arr[6] = [None, Tile(), Tile(), B[0], None, None, None, Tile()]

    arr[7] = [None, None]
    arr[7] += [Tile() for i in range(6)]

    s = Stage('stage7', arr, 3, 1)
    s.save('stage7')