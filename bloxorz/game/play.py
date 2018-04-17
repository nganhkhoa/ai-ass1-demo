from bloxorz.stages.GenStage import GenStage

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T

from bloxorz.game.mode import mode as m
import bloxorz.solver.solver as solver

import pickle


def load(f):
    try:
        s = pickle.load(open("./raw/{}".format(f), "rb"))
    except FileNotFoundError:
        print("[+] No stage is found, proceed generating stages")
        GenStage()
        try:
            s = pickle.load(open("./raw/{}".format(f), "rb"))
        except FileNotFoundError:
            print("--- Cannot generate: {}".format(f))
            exit(-2)
    # print(s)
    return s


def play(f, mode=m.bfs):
    s = load(f)

    if mode == m.bfs:
        print("[+] Solving with bfs now")
        solver.bfs(s)

    elif mode == m.dfs:
        print("[+] Solving with dfs now")
        solver.dfs(s)

    elif mode == m.hill:
        print("[+] Solving with hill climbing now")
        solver.hill(s)

    elif mode == m.annealing:
        print("[+] Simulated Annealing?")
        solver.annealing(s)

    elif mode == m.best:
        print("[+] Someone says best first?")
        solver.best(s)

    else:
        print("[?] LOL what algorithm")
