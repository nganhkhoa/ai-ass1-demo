from enum import Enum, auto


class TileType(Enum):
    normal = auto()
    goal = auto()
    gate = auto()
    opengate = auto()
    closegate = auto()
    bridge = auto()
    split = auto()
