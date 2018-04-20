from .TileType import TileType as T


class Tile:
    def __init__(this, t=T.normal, info=None, others=None, extra=None):
        this.type = t

        if t == T.bridge:
            this.valid = info

        elif t == T.split:
            this.split_place = info  # [x,y,x,y]

        elif t == T.soft_button or t == T.hard_button:
            this.toggle = info

        elif t == T.soft_special_button or t == T.hard_special_button:
            this.open = info
            this.close = others

        elif t == T.soft_hell_button or t == T.hard_hell_button:
            this.toggle = info
            this.open = others
            this.close = extra

        else:
            pass

    def __repr__(this):
        t = this.type
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

        elif t == T.bridge and this.valid:
            return "\033[33;43m \033[0m"

        elif t == T.bridge:
            return " "

        elif t == T.split:
            return "S"

        elif t == T.goal:
            return "\033[36;46m \033[0m"

        else:
            return "\033[37;47m \033[0m"

    def setValid(this, v):
        this.valid = v

    def getValid(this):
        return this.valid

    def isGoal(this):
        return this.type == T.goal

    def trigger(this, standing):

        t = this.type

        if t == T.soft_button:
            for tile in this.toggle:
                tile.valid = not tile.valid

        elif t == T.soft_special_button:
            for tile in this.open:
                tile.valid = True
            for tile in this.close:
                tile.valid = False

        elif t == T.soft_hell_button:
            for tile in this.toggle:
                tile.valid = not tile.valid
            for tile in this.open:
                tile.valid = True
            for tile in this.close:
                tile.valid = False

        elif t == T.hard_button and standing:
            for tile in this.toggle:
                tile.valid = not tile.valid

        elif t == T.hard_special_button and standing:
            for tile in this.open:
                tile.valid = True
            for tile in this.close:
                tile.valid = False

        elif t == T.hard_hell_button and standing:
            for tile in this.toggle:
                tile.valid = not tile.valid
            for tile in this.open:
                tile.valid = True
            for tile in this.close:
                tile.valid = False

        elif t == T.soft_ground and standing:
            # watch out, you'll fall
            raise Exception("Fall")

        elif t == T.bridge and this.valid == False:
            raise Exception("HiddenBridge")

        elif t == T.split:
            return this.split_place

        else:
            pass

        return None
