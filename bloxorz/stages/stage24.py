from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage24():
    B1 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB1 = Tile(T.bridge, False)
    SB2 = Tile(T.bridge, False)

    arr = [[] for i in range(8)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(10)]
    arr[0] += [Tile(), Tile(), Tile(), Tile()]

    arr[1] = [None, None, None, SB1]
    arr[1] += [Tile() for i in range(7)]
    arr[1] += [Tile(T.hard_special_button, B1, []), Tile(), Tile(T.split, [6,5,6,7])]

    arr[2] = [None, Tile(), B1[0], B1[1], Tile(), Tile(T.hard_special_button, [SB2], []), Tile(), 
                None, None, None, Tile(), Tile(), Tile(), Tile()]

    arr[3] = [Tile(T.hard_special_button, [SB1], []), Tile(), None, None, Tile(), Tile()]
    arr[3] += [None for i in range(6)]
    arr[3] += [Tile()]

    arr[4] = [Tile(), Tile(), None, None, Tile()]
    arr[4] += [None for i in range(6)]
    arr[4] += [Tile()]

    arr[5] = [Tile() for i in range(5)]
    arr[5] += [None for i in range(5)]
    arr[5] += [Tile(), Tile(), Tile()]

    arr[6] = [Tile(), Tile(), Tile(), None, None, 
                Tile(), Tile(), Tile(), B2[0], B2[1], Tile(), Tile(T.goal), Tile()]

    arr[7] = [None for i in range(5)]
    arr[7] += [Tile(T.hard_special_button, B2, []), Tile(), SB2, None, None, Tile(), Tile(), Tile()]

    s = Stage('stage24', arr, 2, 1)
    s.save('stage24')