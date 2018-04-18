from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage5():
    B1 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B2 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    B3 = [Tile(T.bridge, True), Tile(T.bridge, True)]
    arr = [[] for i in range(10)]

    arr[0] = [None for i in range(11)]
    arr[0] += [Tile() for i in range(4)]

    arr[1] = [None, Tile(), Tile(), Tile(), Tile(), B1[0], B1[1],
              Tile(), Tile(T.soft_button, B1)]
    arr[1] += [Tile() for i in range(6)]

    arr[2] = [None] + [Tile() for i in range(4)]
    arr[2] += [None for i in range(7)]
    arr[2] += [Tile() for i in range(3)]

    arr[3] = [None, Tile(), Tile(),
              Tile(T.soft_special_button, B3, []), Tile()]

    arr[4] = [None] + [Tile() for i in range(4)]

    arr[5] = [None, None, None, Tile(), Tile(), Tile(),
              Tile(T.soft_special_button, [], B3), Tile(), B2[0], B2[1],
              Tile(), Tile(), Tile()]

    arr[6] = [None for i in range(10)]
    arr[6] += [Tile() for i in range(4)]
    arr[6].append(Tile(T.soft_special_button, B3, []))

    arr[7] = [Tile() for i in range(3)]
    arr[7] += [None for i in range(7)]
    arr[7] += [Tile() for i in range(5)]

    arr[8] = [Tile(), Tile(T.goal)] + [Tile() for i in range(3)]
    arr[8] += [B3[0], B3[1]]
    arr[8] += [Tile() for i in range(6)]

    arr[9] = [Tile() for i in range(4)]

    s = Stage('stage5', arr, 13, 1)
    s.save('stage5')
