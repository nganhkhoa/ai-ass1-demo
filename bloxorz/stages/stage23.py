from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage23():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB = Tile(T.bridge, True)
    SB1 = Tile(T.bridge, False)
    SB2 = Tile(T.bridge, False)
    SB3 = Tile(T.bridge, False)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None, Tile(), Tile(), Tile()]
    arr[0] += [None for i in range(8)]
    arr[0] += [Tile(), Tile(), Tile()]

    arr[1] = [None, Tile(), Tile(T.hard_button, [SB3], []), Tile()]
    arr[1] += [None for i in range(8)]
    arr[1] += [Tile(), Tile(T.soft_button, B2, ), Tile()] #!!!!!!!!!!!!open B2, toggle SB1

    arr[2] = [None, Tile(), Tile(), Tile(), 
                None, None, None, Tile(), Tile(), Tile(), 
                B1[0], B1[1], Tile(), Tile(), Tile()]

    arr[3] = [SB2, Tile(), Tile(), Tile(), SB3, 
                None, None, Tile(), Tile(T.goal), Tile(), 
                None, None, Tile(), Tile(), Tile(T.soft_button, [], [B1[0], B1[1], SB])]

    arr[4] = [Tile(), None, None, None, 
                Tile(), None, None, Tile(), Tile(), Tile(), 
                None, None, None, None, Tile()]

    arr[5] = [Tile(T.soft_button, [SB2], B2), None, None, None, 
                Tile(), None, Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground), 
                None, None, None, None, Tile()]

    arr[6] = [Tile(), B2[0], B2[1], Tile(), Tile(), Tile()]
    arr[6] += [Tile(T.soft_ground) for i in range(5)]
    arr[6] += [Tile(), Tile(), Tile(), SB]

    arr[7] = [None, None, None, Tile(), Tile(), Tile()]
    arr[7] += [Tile(T.soft_ground) for i in range(5)]
    arr[7] += [Tile(), Tile(T.split, [7,12,2,2]), Tile()]

    arr[8] = [None, None, None, Tile(), Tile(), Tile()]
    arr[8] += [Tile(T.soft_ground) for i in range(5)]
    arr[8] += [Tile(), Tile(), Tile()]

    arr[9] = [None, None, None]
    arr[9] += [Tile() for i in range(5)]
    arr[9] += [SB1]

    s = Stage('stage23', arr, 7, 4)
    s.save('stage23')