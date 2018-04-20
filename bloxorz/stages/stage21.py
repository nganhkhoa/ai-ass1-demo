from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage21():
    HB = Tile(T.bridge, False)
    HB1 = Tile(T.bridge, False)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(8)]
    arr[0] += [Tile(), Tile()]

    arr[1] = [None for i in range(7)]
    arr[1] += [Tile(), Tile(), Tile()]

    arr[2] = [Tile(), Tile(), None, None]
    arr[2] += [Tile() for i in range(6)]

    arr[3] = [Tile() for i in range(6)]
    arr[3] += [None, None, Tile()]

    arr[4] = [Tile(), Tile(), Tile(), Tile(), 
                None, None, None, None, Tile(), 
                None, None, None, Tile(), Tile(), Tile()]

    arr[5] = [None, Tile(), Tile()]
    arr[5] += [None for i in range(5)]
    arr[5] += [Tile(T.hard_button, [HB]), Tile(), Tile(), Tile(), Tile(), Tile(T.goal), Tile()]

    arr[6] = [None, None, Tile()]
    arr[6] += [None for i in range(5)]
    arr[6] += [Tile(T.hard_button, [HB1]), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[7] = [None, None, Tile(), Tile(), Tile(), HB1, None, None, Tile(), Tile()]

    arr[8] = [None, None, None, Tile(), Tile(), Tile(), None, None, Tile(), Tile()]

    arr[9] = [None, None, None, HB]
    arr[9] += [Tile() for i in range(6)]

    s = Stage('stage21', arr, 3, 1)
    s.save('stage21')