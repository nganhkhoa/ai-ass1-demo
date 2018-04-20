from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage17():
    SB = Tile(T.bridge, False)
    HB1 = Tile(T.bridge, False)
    HB2 = Tile(T.bridge, False)
    HB3 = Tile(T.bridge, False)

    arr = [[] for i in range(10)]  # type: List[List[Tile]]

    arr[0] = [Tile(), Tile(), Tile()]

    arr[1] = [Tile() for i in range(9)]
    arr[1] += [None, None, None, Tile(), Tile(), Tile()]

    arr[2] = [Tile(), Tile(), Tile()]
    arr[2] += [None, None, None, None, HB1, 
                Tile(), Tile(), Tile(), Tile(), Tile(), Tile(T.goal), Tile()]

    arr[3] = [Tile(), Tile(), Tile()]
    arr[3] += [None for i in range(9)]
    arr[3] += [Tile(T.hard_special_button, [], HB3), Tile(T.hard_special_button, HB3, []), Tile()]

    arr[4] = [Tile(), Tile(), Tile()]
    
    arr[5] = [Tile(), Tile(), Tile()]

    arr[6] = [Tile(), Tile(), Tile(), 
                None, None, None, HB3, 
                Tile(), Tile(), Tile(), Tile(), Tile(), Tile(T.hard_special_button, HB1, [])]
    
    arr[7] = [Tile() for i in range(8)]
    arr[7] += [SB, None, None, Tile(), Tile()]

    arr[8] = [Tile(), Tile(T.soft_special_button, SB, []), Tile()]
    arr[8] += [None for i in range(8)]
    arr[8] += [Tile(), Tile()]

    arr[9] = [Tile(), Tile(), Tile()]
    arr[9] += [None for i in range(8)]
    arr[9] += [Tile(), Tile(T.hard_special_button, HB2, SB)]

    s = Stage('stage17', arr, 1, 1)
    s.save('stage17')