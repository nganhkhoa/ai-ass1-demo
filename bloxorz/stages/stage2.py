from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage2():
    arr = [[] for i in range(6)]  # type: List[List[Tile]]
    bridge_left = [Tile(T.bridge, False), Tile(T.bridge, False)]
    bridge_right = [Tile(T.bridge, False), Tile(T.bridge, False)]

    arr[0] = [None, None, None, None, None, None,
              Tile(), Tile(), Tile(), Tile(),
              None, None, Tile(), Tile(), Tile()]

    arr[1] = [Tile(), Tile(), Tile(), Tile(), None, None, Tile(), Tile(),
              Tile(T.hard_special_button, bridge_right, []), Tile(),
              None, None, Tile(), Tile(T.goal), Tile()]

    arr[2] = [Tile(), Tile(), Tile(T.soft_button, bridge_left), Tile(),
              None, None, Tile(), Tile(), Tile(), Tile(),
              None, None, Tile(), Tile(), Tile()]

    arr[3] = [Tile(), Tile(), Tile(), Tile(),
              None, None, Tile(), Tile(), Tile(), Tile(),
              None, None, Tile(), Tile(), Tile()]

    arr[4] = [Tile(), Tile(), Tile(), Tile(),
              bridge_left[0], bridge_left[1], Tile(), Tile(), Tile(), Tile(),
              bridge_right[0], bridge_right[1], Tile(), Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), Tile(),
              Tile(), Tile(), Tile(), Tile(),
              None, None, None, None, None, None]

    s = Stage('stage2', arr, 4, 1)
    s.save('stage2')