from bloxorz.stages.GenStage import GenStage

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T

from bloxorz.solver.State import State

from bloxorz.game.mode import mode as m
from bloxorz.solver.Solver import Solver

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
    stage = load(f)
    init = State(stage)

    problem = Solver(init, mode)
    problem.solve()
    print(problem)
