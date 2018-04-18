from bloxorz.stages.GenStage import GenStage

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T

from bloxorz.solver.State import State

from bloxorz.game.mode import mode as m
from bloxorz.solver.Solver import Solver

from bloxorz.solver.moves import moves

import pickle
# from bloxorz.solver.Getch import _Getch

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


def get_key(getch):
    line = getch()


def play(f, mode=None):
    stage = load(f)
    init = State(stage)
    getch = _Getch

    if mode is None:
        s = init
        while True:
            print("\033[1H", end="")
            print("\033[J", end="")
            print(s)
            print("1. Up; 2. Down; 3. Left; 4. Right")
            # key = get_key(getch)
            try:
                key = moves(int(input()))
            except ValueError:
                break
            s.move(key)
            input()

    else:
        problem = Solver(init, mode)
        problem.solve()
        print(problem)
