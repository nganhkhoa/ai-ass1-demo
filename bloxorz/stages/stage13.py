from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage13():
    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [Tile(), Tile(), Tile(), Tile(T.soft_ground)]
    arr[0] += [Tile() for i in range(4)]
    arr[0] += [Tile(T.soft_ground)]
    arr[0] += [Tile() for i in range(4)]

    arr[1] = [Tile(), Tile()]
    arr[1] += [None for i in range(8)]
    arr[1] += [Tile(), Tile(), Tile()]

    arr[2] = [Tile(), Tile()]
    arr[2] += [None for i in range(9)]
    arr[2] += [Tile(), Tile(), Tile()]

    arr[3] = [Tile(), Tile(), Tile()]
    arr[3] += [None, None, None]
    arr[3] += [Tile(), Tile(), Tile(), None, None]
    arr[3] += [Tile(), Tile(), Tile()]

    arr[4] = [Tile(), Tile(), Tile(), 
                Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground), 
                Tile(), Tile(T.goal), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), None, None, Tile(T.soft_ground), 
                Tile(), Tile(), Tile(), None, None, Tile()]

    arr[6] = [None, None, Tile(), None, None]
    arr[6] += [Tile(T.soft_ground) for i in range(5)]
    arr[6] += [Tile(), Tile()]

    arr[7] = [None, None, Tile(), Tile(), Tile(), 
                Tile(T.soft_ground), Tile(T.soft_ground), Tile(), 
                Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground)]

    arr[8] = [None, None, None, Tile(), Tile()]
    arr[8] += [Tile(T.soft_ground) for i in range(6)]

    arr[9] = [None, None, None, Tile(), Tile(), Tile(), None, None, Tile(), Tile()]

    s = Stage('13', arr, 3, 12)
    s.save('13')