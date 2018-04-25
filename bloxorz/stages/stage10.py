from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage10():
    HB = [Tile(T.bridge, False), 
            Tile(T.bridge, False), 
            Tile(T.bridge, False), 
            Tile(T.bridge, False)]

    SB = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [Tile(), Tile(), Tile()]
    arr[0] += [None for i in range(5)]
    arr[0] += [Tile() for i in range(6)]

    arr[1] = [Tile(), Tile(T.goal), Tile()]
    arr[1] += [SB[0], SB[1], Tile(), HB[0], HB[1]]
    arr[1] += [Tile(), Tile(), Tile(), Tile(), Tile(T.split, [1,9,1,12]), Tile()]

    arr[2] = [Tile(), Tile(), Tile()]
    arr[2] += [None for i in range(5)]
    arr[2] += [Tile() for i in range(4)]
    arr[2].append(HB[2])

    arr[3] = [None for i in range(9)]
    arr[3] += [Tile(), Tile(), Tile(), HB[3]]

    arr[4] = [None for i in range(11)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [None for i in range(12)]
    arr[5].append(Tile())

    arr[6] = [None for i in range(12)]
    arr[6].append(Tile())

    arr[7] = [None for i in range(11)]
    arr[7] += [Tile(), Tile()]

    arr[8] = [None for i in range(4)]
    arr[8] += [Tile() for i in range(5)]
    arr[8] += [None, None, Tile(), Tile()]

    arr[9] = [None for i in range(4)]
    arr[9] += [Tile(), Tile(T.soft_button, SB), None, None]
    arr[9] += [Tile(), Tile(), Tile(), Tile(T.hard_button, HB), Tile()]

    s = Stage('stage10', arr, 1, 9)
    s.save('stage10')