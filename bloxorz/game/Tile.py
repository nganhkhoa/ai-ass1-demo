from .TileType import TileType as T


class Tile():
    def __init__(this, t=T.normal, trg=[], valid=True, split_place=None):
        this.type = t
        this.trg = trg
        this.valid = valid
        this.split_place = split_place

    def setValid(this, v):
        this.valid = v

    def getValid(this):
        return this.valid

    def trigger(this):
        if this.type == T.closegate:
            # close all tile associate
            for trg in this.trg:
                trg.setValid(False)
        elif this.type == T.opengate:
            # open all tile associate
            for trg in this.trg:
                trg.setValid(True)
        elif this.type == T.gate:
            # set all gate associate to
            # another state
            for trg in this.trg:
                trg.setValid(not trg.getValid())
        elif this.type == T.split:
            # return place after split
            return this.split_place
        else:
            pass

        return None
