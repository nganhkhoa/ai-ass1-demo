from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage12():
    H1 = [Tile(T.bridge, False)]
    H2 = [Tile(T.bridge, False)]

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [None for i in range(12)]
    arr[0].append(Tile(T.hard_button, H2))

    arr[1] = [None for i in range(5)]
    arr[1] += [Tile(), Tile(), Tile(), None, None, Tile(), Tile(), Tile()]

    arr[2] = [None for i in range(5)]
    arr[2] += [Tile(), Tile(T.hard_button, H1), Tile(), Tile(), Tile(), Tile(), Tile(), H1[0]]

    arr[3] = [None, None, None]
    arr[3] += [Tile() for i in range(5)]
    arr[3] += [None, None, Tile(), Tile()]

    arr[4] = [None, None, None, Tile(), Tile(T.goal), Tile(), H2[0]]
    arr[4] += [None for i in range(3)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [Tile() for i in range(6)]
    arr[5] += [None, None, None]
    arr[5] += [Tile() for i in range(4)]

    arr[6] = [Tile() for i in range(4)]
    arr[6] += [None for i in range(5)]
    arr[6] += [Tile() for i in range(4)]

    arr[7] = [Tile() for i in range(4)]
    arr[7] += [None, None]
    arr[7] += [Tile() for i in range(5)]
    
    arr[8] = [None for i in range(5)]
    arr[8] += [Tile(), Tile(), Tile()]

    arr[9] = [None for i in range(5)]
    arr[9] += [Tile(), Tile(), Tile()]

    s = Stage('stage12', arr, 6, 2)
    s.save('stage12')