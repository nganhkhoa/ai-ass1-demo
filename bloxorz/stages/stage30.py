from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage30():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, False), Tile(T.bridge, False)]
    SB1 = Tile(T.bridge, False)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None, None, None]
    arr[0] += [Tile() for i in range(5)]
    arr[0] += [Tile(T.soft_ground), Tile(T.soft_ground), Tile(), Tile(), Tile(), Tile()]

    arr[1] = [None, None, None, Tile(), Tile(T.goal), Tile(), Tile()]
    arr[1] += [None for i in range(5)]
    arr[1] += [Tile(T.soft_ground), Tile()]

    arr[2] = [None, None, None, Tile(), Tile(), Tile()]
    arr[2] += [None for i in range(6)]
    arr[2] += [Tile(T.soft_ground), Tile(), Tile(T.hard_special_button, B2, B1)]

    arr[3] = [None for i in range(7)]
    arr[3] += [Tile(T.soft_ground), Tile(), Tile(), B1[0], B1[1], Tile(), Tile(), Tile()]

    arr[4] = [None, None, Tile()]
    arr[4] += [None for i in range(4)]
    arr[4] += [Tile(T.soft_ground), Tile(T.soft_ground)]
    arr[4] += [None for i in range(5)]
    arr[4] += [Tile()]

    arr[5] = [None, Tile(T.hard_special_button, B1, []), Tile(), Tile(T.soft_ground), 
                None, None, None, Tile(T.soft_ground), Tile(T.soft_ground)]
    arr[5] += [None for i in range(5)]
    arr[5] += [Tile()]

    arr[6] = [Tile(T.soft_ground) for i in range(4)]
    arr[6] += [None, None, None, Tile(), Tile()]
    arr[6] += [B2[0], None, None, B2[1]]
    arr[6] += [Tile(), Tile()]

    arr[7] = [Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground), 
                Tile(), Tile(T.soft_ground), Tile(), Tile(T.soft_ground), Tile(T.soft_ground), 
                Tile(), Tile(T.soft_ground), None, None, Tile(T.hard_button, [SB1]), Tile(), SB1]

    arr[8] = [Tile()]
    arr[8] += [Tile(T.soft_ground) for i in range(11)]
    arr[8] += [Tile()]

    arr[9] = [None, Tile(T.soft_ground), Tile(), 
                Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground), 
                None, None, Tile(T.soft_ground), Tile(T.soft_ground), 
                Tile(T.soft_ground), Tile(T.soft_ground), Tile()]

    s = Stage('stage30', arr, 4, 2)
    s.save('stage30')