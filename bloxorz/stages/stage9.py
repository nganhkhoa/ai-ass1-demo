from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage9():
    arr = [[] for i in range(5)]  # type: List[List[Tile]]

    arr[0] = [Tile() for i in range(4)]
    arr[0] += [None, None, None, Tile(), None, None, None]
    arr[0] += [Tile() for i in range(4)]

    arr[1] = [Tile(), Tile(), Tile(), Tile()]
    arr[1] += [None, None, None, Tile(), None, None, None]
    arr[1] += [Tile(), Tile(), Tile(T.split, [1,2,1,12]), Tile()]

    arr[2] = [Tile() for i in range(15)]

    arr[3] = [None for i in range(6)]
    arr[3] += [Tile(), Tile(T.goal), Tile()]
    
    arr[4] = [None for i in range(6)]
    arr[4] += [Tile(), Tile(), Tile()]

    s = Stage('stage9', arr, 1, 1)
    s.save('stage9')