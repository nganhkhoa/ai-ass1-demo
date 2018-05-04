from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage26():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(9)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(5)]
    arr[0] += [Tile() for i in range(4)]
    arr[0] += [None for i in range(4)]
    arr[0] += [Tile(T.split, [3,12,5,10])]

    arr[1] = [None for i in range(5)]
    arr[1] += [Tile(), Tile(), Tile(T.soft_special_button, [], B1), 
                Tile(), Tile(), Tile(), None, None, Tile()]

    arr[2] = [None for i in range(4)]
    arr[2] += [Tile() for i in range(7)]
    arr[2] += [None, None, Tile()]
    
    arr[3] = [Tile(), Tile(), B1[0], B1[1], Tile(), Tile(), Tile(), Tile(), 
                None, None, Tile(), Tile(), Tile(), Tile()]

    arr[4] = [Tile(), Tile(), Tile(), B2[0], None, None, Tile(), None, None, None, Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), None, None, None, Tile(), None, None, None, Tile()]
    
    arr[6] = [None, Tile()]
    arr[6] += [None for i in range(4)]
    arr[6] += [Tile(), Tile(), Tile()]

    arr[7] = [None, Tile(T.hard_special_button, B2, [])]
    arr[7] += [None for i in range(4)]
    arr[7] += [Tile(), Tile(T.goal), Tile(), B2[1]]

    arr[8] = [None for i in range(6)]
    arr[8] += [Tile(), Tile(), Tile()]

    s = Stage('26', arr, 5, 10)
    s.save('26')