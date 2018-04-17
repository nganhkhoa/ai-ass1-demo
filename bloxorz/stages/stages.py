from typing import List

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T


def stage1():
    arr = [[] for i in range(6)]  # type: List[List[Tile]]

    arr[0] = [Tile(), Tile(), Tile()]

    arr[1] = [Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]

    arr[2] = [Tile(), Tile(), Tile(), Tile(),
              Tile(), Tile(), Tile(), Tile(), Tile()]

    arr[3] = [None, Tile(), Tile(), Tile(), Tile(),
              Tile(), Tile(), Tile(), Tile(), Tile()]

    arr[4] = [None, None, None, None, None,
              Tile(), Tile(), Tile(T.goal), Tile(), Tile()]

    arr[5] = [None, None, None, None, None,
              None, Tile(), Tile(), Tile()]

    s = Stage('stage1', arr, 1, 1)
    s.save('stage1')


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

    s = Stage('stage2', arr, 1, 4)
    s.save('stage2')


def stage3():
    arr = [[] for i in range(6)]

    arr[0] = [None for i in range(6)]
    arr[0] += [Tile() for i in range(7)]

    arr[1] = [Tile() for i in range(4)] + [None, None]
    arr[1] += [Tile() for i in range(3)] + [None, None, Tile(), Tile()]

    arr[2] = [Tile() for i in range(9)] + [None, None]
    arr[2] += [Tile() for i in range(4)]

    arr[3] = [Tile() for i in range(4)] + [None for i in range(7)]
    arr[3] += [Tile(), Tile(), Tile(T.goal), Tile()]

    arr[4] = [Tile() for i in range(4)] + [None for i in range(7)]
    arr[4] += [Tile(), Tile(), Tile(), Tile()]

    arr[5] = [None for i in range(12)] + [Tile(), Tile(), Tile()]

    s = Stage('stage3', arr, 1, 3)
    s.save('stage3')


def stage4():
    arr = [[] for i in range(9)]

    arr[0] = [None, None, None] + [Tile(T.soft_ground) for i in range(7)]

    arr[1] = [None, None, None] + [Tile(T.soft_ground) for i in range(7)]

    arr[2] = [Tile() for i in range(4)] + [None for i in range(5)]
    arr[2] += [Tile() for i in range(3)]

    arr[3] = [Tile(), Tile(), Tile()] + [None for i in range(7)]
    arr[3] += [Tile(), Tile()]

    arr[4] = [Tile(), Tile(), Tile()] + [None for i in range(7)]
    arr[4] += [Tile(), Tile()]

    arr[5] = [Tile(), Tile(), Tile(), None, None]
    arr[5] += [Tile() for i in range(4)]
    arr[5] += [Tile(T.soft_ground) for i in range(5)]

    arr[6] = [Tile(), Tile(), Tile(), None, None]
    arr[6] += [Tile() for i in range(4)]
    arr[6] += [Tile(T.soft_ground) for i in range(5)]

    arr[7] = [None for i in range(5)]
    arr[7] += [Tile(), Tile(T.goal), Tile(), None, None,
               Tile(T.soft_ground), Tile(T.soft_ground),
               Tile(), Tile(T.soft_ground)]

    arr[8] = [None for i in range(5)] + [Tile(), Tile(), Tile(), None, None]
    arr[8] += [Tile(T.soft_ground) for i in range(4)]

    s = Stage('stage4', arr, 1, 5)
    s.save('stage4')


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

    s = Stage('stage5', arr, 1, 13)
    s.save('stage5')
