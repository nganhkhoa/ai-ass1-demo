from enum import Enum, auto


class TileType(Enum):
    normal = auto()
    goal = auto()
    split = auto()
    soft_ground = auto()
    bridge = auto()
    soft_gate = auto()
    soft_open_gate = auto()
    soft_close_gate = auto()
    hard_gate = auto()
    hard_open_gate = auto()
    hard_close_gate = auto()
