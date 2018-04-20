from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage14():
    HB1 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    HB2 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(8)]
    arr[0] += [Tile(), Tile(), Tile()]

    arr[1] = [None, None, None, Tile(), Tile(), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[2] = [Tile(), HB1[0], HB1[1]]
    arr[2] += [Tile() for i in range(11)]
    
    arr[3] = [Tile(), HB2[0], HB2[1], Tile(), Tile(), Tile()]
    arr[3] += [None for i in range(6)]
    arr[3] += [Tile(T.hard_button, HB1), Tile()]

    arr[4] = [Tile()]
    arr[4] += [None for i in range(11)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [Tile()]
    arr[5] += [None for i in range(11)]
    arr[5] += [Tile(), Tile()]

    arr[6] = [Tile()]
    arr[6] += [None for i in range(7)]
    arr[6] += [Tile() for i in range(6)]

    arr[7] = [Tile() for i in range(5)]
    arr[7] += [None, None, None, Tile(), Tile(), Tile()]

    arr[8] = [None, Tile(), Tile(), Tile(T.goal), Tile(), None, None, None, Tile(), Tile(), Tile()]

    arr[9] = [None, None, Tile(), Tile(), Tile(), None, None, None]
    arr[9] += [Tile() for i in range(5)]
    arr[9].append(Tile(T.hard_button, HB2))

    s = Stage('stage14', arr, 2, 4)
    s.save('stage14')