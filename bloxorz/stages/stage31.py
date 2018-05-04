from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage31():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B3 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    B4 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B5 = [Tile(T.bridge, False), Tile(T.bridge, False), Tile(T.bridge, False)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(11)]
    arr[0] += [Tile(), Tile(), Tile(), B5[0]]

    arr[1] = [None, Tile(), Tile(), Tile(), 
                None, None, None, None, Tile(T.hard_button, B2), 
                None, None, Tile(), Tile(T.goal), Tile(), B5[1]]

    arr[2] = [None, Tile(), Tile(), Tile(), B1[0], B1[1], 
                Tile(), Tile(), Tile(), B2[0], B2[1], Tile(), Tile(), Tile(), B5[2]]

    arr[3] = [None, Tile(), Tile(), Tile(), None, None, 
                Tile(), Tile(), Tile(), None, None, None, Tile()]

    arr[4] = [None, Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground), None, None, 
                Tile(T.soft_special_button, [], [B1[0],B1[1],B2[0],B2[1],B3[0],B3[1],B4[0],B4[1]]), 
                Tile(), Tile(), None, None, None, Tile(T.soft_ground)]

    arr[5] = [None, None, Tile(T.soft_ground), None, None, None, Tile(), Tile(), Tile(), 
                None, None, Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground)]

    arr[6] = [None, None, Tile(), None, None, None, Tile(), Tile(), Tile(), 
                None, None, Tile(), Tile(), Tile()]

    arr[7] = [Tile(), Tile(), Tile(), Tile(), B3[0], B3[1], Tile(), 
                Tile(T.soft_special_button, [], [B1[0],B1[1],B2[0],B2[1],B3[0],B3[1],B4[0],B4[1]]), 
                Tile(), B4[0], B4[1], Tile(), Tile(), Tile()]

    arr[8] = [Tile(), Tile(), Tile(T.hard_special_button, B5, B1), Tile(), 
                None, None, Tile(T.hard_button, B3), 
                None, None, None, None, Tile(), Tile(), Tile()]

    arr[9] = [Tile(), Tile(), Tile(), Tile()]

    s = Stage('31', arr, 7, 12)
    s.save('31')