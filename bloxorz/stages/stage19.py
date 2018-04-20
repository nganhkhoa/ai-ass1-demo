from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage19():
    SB1 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB2 = [Tile(T.bridge, True), Tile(T.bridge, True)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None]
    arr[0] += [Tile() for i in range(9)]
    arr[0] += [Tile(T.soft_button, SB1), Tile(), Tile(), Tile(), Tile()]

    arr[1] = [None for i in range(5)]
    arr[1] += [Tile(), Tile()]
    arr[1] += [None for i in range(6)]
    arr[1] += [Tile(), Tile()]

    arr[2] = [None for i in range(5)]
    arr[2] += [Tile(), Tile()]
    arr[2] += [None for i in range(6)]
    arr[2] += [Tile(), Tile()]

    arr[3] = [None for i in range(13)]
    arr[3] += [Tile(), Tile()]
    
    arr[4] = [None for i in range(13)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), 
                None, None, Tile(), Tile(), SB1[0], SB1[1], 
                Tile(), Tile(T.soft_special_button, [], SB2), Tile(), Tile(), Tile(), Tile()]

    arr[6] = [Tile(), Tile(T.goal), Tile(), None, None, Tile(), Tile()]

    arr[7] = [Tile(), Tile(), Tile(), None, None, Tile(), Tile()]

    arr[8] = [None, Tile(), Tile(), None, None, Tile(), Tile()]

    arr[9] = [None, Tile(), SB2[0], SB2[1]]
    arr[9] += [Tile() for i in range(6)]
    arr[9] += [Tile(T.soft_special_button, SB2, []), Tile(), Tile(), Tile()]

    s = Stage('stage19', arr, 0, 1)
    s.save('stage19')