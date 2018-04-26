from .TileType import TileType as T


class Tile:
    def __init__(self, t=T.normal, info=None, others=None, extra=None):
        self.type = t

        if t == T.bridge:
            self.valid = info

        elif t == T.split:
            self.split_place = info  # [x,y,x,y]

        elif t == T.soft_button or t == T.hard_button:
            self.toggle = info

        elif t == T.soft_special_button or t == T.hard_special_button:
            self.open = info
            self.close = others

        elif t == T.soft_hell_button or t == T.hard_hell_button:
            self.toggle = info
            self.open = others
            self.close = extra

        else:
            pass

    def __repr__(self):
        t = self.type
        if t == T.soft_button or \
           t == T.soft_special_button or \
           t == T.soft_hell_button:
            return "O"

        elif t == T.hard_button or \
             t == T.hard_special_button or \
             t == T.hard_hell_button:
            return "X"

        elif t == T.soft_ground:
            return "\033[31;41m \033[0m"

        elif t == T.bridge and self.valid:
            return "\033[33;43m \033[0m"

        elif t == T.bridge:
            return " "

        elif t == T.split:
            return "S"

        elif t == T.goal:
            return "\033[36;46m \033[0m"

        else:
            return "\033[37;47m \033[0m"

    def setValid(self, v):
        self.valid = v

    def getValid(self):
        return self.valid

    def isGoal(self):
        return self.type == T.goal

    def trigger(self, standing):

        t = self.type

        if t == T.soft_button:
            for tile in self.toggle:
                tile.valid = not tile.valid

        elif t == T.soft_special_button:
            for tile in self.open:
                tile.valid = True
            for tile in self.close:
                tile.valid = False

        elif t == T.soft_hell_button:
            for tile in self.toggle:
                tile.valid = not tile.valid
            for tile in self.open:
                tile.valid = True
            for tile in self.close:
                tile.valid = False

        elif t == T.hard_button and standing:
            for tile in self.toggle:
                tile.valid = not tile.valid

        elif t == T.hard_special_button and standing:
            for tile in self.open:
                tile.valid = True
            for tile in self.close:
                tile.valid = False

        elif t == T.hard_hell_button and standing:
            for tile in self.toggle:
                tile.valid = not tile.valid
            for tile in self.open:
                tile.valid = True
            for tile in self.close:
                tile.valid = False

        elif t == T.soft_ground and standing:
            # watch out, you'll fall
            raise Exception("Fall")

        elif t == T.bridge and self.valid == False:
            raise Exception("HiddenBridge")

        # notice this case,Will every block split only when standing?
        elif t == T.split and standing:
            return self.split_place

        #else:
            #pass

        return None
