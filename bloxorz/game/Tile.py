from .TileType import TileType as T


class Tile():
    def __init__(this, t=T.normal, trg=[], valid=True):
        this.type = t
        this.trg = trg
        this.valid = valid

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
            pass
        else:
            pass
