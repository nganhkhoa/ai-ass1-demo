from enum import IntEnum, auto


class TileType(IntEnum):
    # normal toggle button
    soft_button = auto()
    hard_button = auto()
    # button with only one scenario
    soft_special_button = auto()
    hard_special_button = auto()

    normal = auto()
    goal = auto()
    split = auto()
    soft_ground = auto()
    bridge = auto()
