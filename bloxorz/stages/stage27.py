from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage27():
    SB1 = Tile(T.bridge, True)
    SB2 = Tile(T.bridge, True)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [Tile(), Tile(), Tile(), None, None, None, None]
    arr[0] += [Tile() for i in range(8)]
    
    arr[1] = [Tile() for i in range(11)]
    arr[1] += [None, None, Tile(), Tile()]

    arr[2] = [Tile(), Tile(), Tile(), None, None, None, None, 
                Tile(), Tile(), None, None, None, None, Tile(), Tile()]

    arr[3] = [None for i in range(12)]
    arr[3] += [Tile(), Tile(T.hard_button, [], [SB1, SB2]), Tile()]

    arr[4] = [None for i in range(12)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), None, None, 
                Tile(T.soft_ground), Tile(T.soft_ground), Tile(T.soft_ground), 
                Tile(T.soft_ground), Tile(), None, None, 
                Tile(T.soft_button, [], [SB1]), Tile(T.soft_button, [], [SB2])]

    arr[6] = [Tile(), Tile(T.goal), Tile()]
    arr[6] += [Tile(T.soft_ground) for i in range(7)]
    arr[6] += [None, None, Tile(), Tile(), Tile()]

    arr[7] = [Tile(), Tile(), Tile()]
    arr[7] += [Tile(T.soft_ground) for i in range(9)]
    arr[7] += [Tile(), Tile(), Tile()]

    arr[8] = [None for i in range(5)]
    arr[8] += [Tile(T.soft_ground) for i in range(7)]
    arr[8] += [Tile(), Tile(), Tile()]

    arr[9] = [None for i in range(6)]
    arr[9] += [SB1, Tile(), Tile(), SB2]

    s = Stage('stage27', arr, 1, 1)
    s.save('stage27')