from .TileType import TileType as T


class Tile():
    def __init__(this, t=T.normal, info=None, others=None):
        this.type = t
        if t == T.normal:
            pass
        if t == T.bridge:
            this.valid = info
        elif t == T.split:
            this.split_place = info
        else:
            # button
            if others is None:
                # a simple button toggle the state every time pressed
                this.toggle = info
            else:
                # a button with constraints
                # either open bridges
                # or close bridges
                this.open = info
                this.close = others

    def setValid(this, v):
        this.valid = v

    def getValid(this):
        return this.valid

    def trigger(this, block):
        t = this.type

        if t == 1:
            # a soft button
            if t == T.soft_button:
                for tile in this.toggle:
                    tile.valid = not tile.valid
            else:
                for tile in this.open:
                    tile.valid = True
                for tile in this.close:
                    tile.valid = False

        elif t == 2 and block.standing():
            # a hard button
            if t == T.hard_button:
                for tile in this.toggle:
                    tile.valid = not tile.valid
            else:
                for tile in this.open:
                    tile.valid = True
                for tile in this.close:
                    tile.valid = False

        elif t == T.soft_ground and block.standing():
            # watch out, you'll fall
            raise Exception("Fall")

        else:
            pass

        return None
