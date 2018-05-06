from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage20():
    SB1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    SB2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB3 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(12)]
    arr[0] += [Tile(), Tile(), Tile()]

    arr[1] = [None, None, Tile(), Tile(), Tile(), SB1[0], SB1[1], 
                Tile(), Tile(), Tile(), SB2[0], SB2[1], Tile(), Tile(), Tile()]

    arr[2] = [None, None, Tile(), Tile(), Tile(), 
                None, None, Tile(T.soft_special_button, [], SB1), Tile(), Tile(), 
                None, None, Tile(), Tile(), Tile()]

    arr[3] = [None, None, Tile(), Tile(), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[4] = [None, None, Tile(), Tile(T.soft_special_button, [], SB1), Tile(), 
                None, None, Tile(T.split, [1,13,7,13]), Tile(), Tile(T.soft_special_button, [], SB1)]

    arr[5] = [None, None, Tile(), Tile(), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[6] = [Tile(), Tile(), Tile(), Tile(), 
                None, None, None, Tile(), Tile(), Tile(), 
                SB3[0], SB3[1], Tile(T.soft_button, SB3), Tile(), Tile()]

    arr[7] = [Tile(), Tile(T.soft_button, SB2)]
    arr[7] += [None for i in range(10)]
    arr[7] += [Tile(), Tile(), Tile()]

    arr[8] = [None for i in range(12)]
    arr[8] += [Tile(), Tile(T.goal), Tile()]

    arr[9] = [None for i in range(12)]
    arr[9] += [Tile(), Tile(), Tile()]

    s = Stage('20', arr, 2, 8)
    s.save('20')