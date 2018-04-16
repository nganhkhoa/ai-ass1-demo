from .Tile import Tile
# from .TileType import TileType as T
from .Block import Block

import pickle


class Stage():
    def __init__(this, name, arr: Tile, x, y):
        this.board = arr
        this.block = Block(x, y)
        this.name = name

    def __repr__(this):
        return this.name

    def save(this, f):
        pickle.dump(this, open("./raw/{}".format(f), "wb"))
