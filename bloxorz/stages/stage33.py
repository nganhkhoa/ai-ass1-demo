from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage33():
    B1 = [Tile(T.bridge, False)]
    B2 = [Tile(T.bridge, True), Tile(T.bridge, True)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(5)]
    arr[0] += [Tile(), Tile(), Tile(T.soft_special_button, [], B2), Tile(), Tile(), Tile()]

    arr[1] = [None for i in range(5)]
    arr[1] += [Tile() for i in range(6)]
    arr[1] += [B1[0]]

    arr[2] = [Tile(), Tile(), Tile(), None, None, Tile(T.soft_special_button, [], B2), 
                Tile(), Tile(), Tile(T.soft_special_button, [], B2)]
    arr[2] += [Tile() for i in range(5)]

    arr[3] = [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), 
                Tile(T.soft_special_button, [], B2), Tile(T.soft_special_button, [], B2), 
                Tile(), Tile(), Tile(T.soft_special_button, [], B2)]

    arr[4] = [None for i in range(5)]
    arr[4] += [Tile(), Tile(), Tile(T.soft_special_button, [], B2), Tile(), Tile(), 
                Tile(T.soft_special_button, [], B2), Tile(), Tile(), Tile()]

    arr[5] = [None for i in range(5)]
    arr[5] += [Tile() for i in range(6)]
    arr[5] += [Tile(T.soft_special_button, [], B2), Tile(), Tile()]

    arr[6] = [Tile(), Tile(), Tile(), None, None]
    arr[6] += [Tile() for i in range(6)]
    arr[6] += [Tile(T.soft_special_button, [], B2), Tile(), Tile(), Tile()]

    arr[7] = [Tile(), Tile(T.goal), Tile(), B2[0], B2[1], 
                Tile(), Tile(T.soft_special_button, [], B2), Tile(), 
                None, None, Tile(), Tile(), Tile(), 
                Tile(T.soft_special_button, [], B2), Tile(T.hard_special_button, B1, [])]

    arr[8] = [Tile(), Tile(), Tile(), None, None, Tile(), Tile(), Tile(), 
                None, None, None, Tile(), Tile(), Tile(), Tile()]

    arr[9] = [Tile(), Tile(), Tile()]
    arr[9] += [None for i in range(9)]
    arr[9] += [Tile(), Tile(), Tile()]

    s = Stage('stage33', arr, 3, 1)
    s.save('stage33')