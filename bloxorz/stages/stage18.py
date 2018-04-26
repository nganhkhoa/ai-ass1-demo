from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage18():
    HB = [Tile(T.bridge, False)]
    SB2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB3 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB4 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(9)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(7)]
    arr[0].append(Tile(T.soft_special_button, SB2, []))

    arr[1] = [Tile(), Tile(), Tile(T.soft_special_button, [], [SB3[0], SB3[1], SB4[0], SB4[1]]), 
                Tile(), None, None, None, Tile()]

    arr[2] = [Tile(), Tile(), Tile(), Tile(), Tile(), None, None, Tile()]

    arr[3] = [Tile(), Tile(T.soft_special_button, [], SB2)]
    arr[3] += [Tile() for i in range(6)]
    arr[3] += [SB2[0], SB2[1], Tile(), Tile(), SB3[0], SB3[1], Tile()]

    arr[4] = [Tile() for i in range(5)]
    arr[4] += [HB[0], None, None, Tile(), None, None, None, Tile()]

    arr[5] = [Tile(), Tile(), Tile(T.soft_special_button, [], [SB3[0], SB3[1], SB4[0], SB4[1]]), 
                Tile(), None, None, None, None, Tile(), None, None, None, Tile()]

    arr[6] = [Tile()]
    arr[6] += [None for i in range(7)]
    arr[6] += [Tile(T.soft_special_button, [SB3[0], SB3[1], SB4[0], SB4[1]], []), 
                None, None, Tile(), Tile(), Tile()]

    arr[7] = [Tile()]
    arr[7] += [None for i in range(9)]
    arr[7] += [Tile(), Tile(), Tile(T.goal), Tile()]

    arr[8] = [Tile(), SB4[0], SB4[1], Tile(T.hard_button, HB)]
    arr[8] += [None for i in range(6)]
    arr[8] += [Tile(), Tile(), Tile(), Tile()]

    s = Stage('stage18', arr, 3, 2)
    s.save('stage18')