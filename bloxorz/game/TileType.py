from enum import IntEnum, auto


class TileType(IntEnum):
    # normal toggle button
    soft_button = 1
    hard_button = 2
    # button with only one scenario
    soft_special_button = 1
    hard_special_button = 2

    normal = auto()
    goal = auto()
    split = auto()
    soft_ground = auto()
    bridge = auto()
