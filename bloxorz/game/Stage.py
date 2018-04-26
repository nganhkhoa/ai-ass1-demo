from .Tile import Tile
# from .TileType import TileType as T
# from .Block import Block

import pickle
from os import path, makedirs


class Stage:
    def __init__(self, name, arr: [Tile], x, y):
        self.name = name
        self.board = arr
        self.start_x = x
        self.start_y = y

    def __repr__(self):
        return self.name

    def save(self, f):
        if not path.exists('./raw/'):
            makedirs('./raw/')
        pickle.dump(self, open("./raw/{}".format(f), "wb"))