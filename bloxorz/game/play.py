from bloxorz.stages.GenStage import GenStage

from bloxorz.game.Stage import Stage
from bloxorz.game.Tile import Tile
from bloxorz.game.TileType import TileType as T
from bloxorz.game.mode import mode as m

from bloxorz.solver.State import State, move
from bloxorz.solver.Solver import Solver
from bloxorz.solver.moves import moves

import pickle
import click


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


def getKey():
    k = click.getchar()

    if k == '\033[A':
        return moves.up
    elif k == '\033[B':
        return moves.down
    elif k == '\033[C':
        return moves.right
    elif k == '\033[D':
        return moves.left

    elif k == ' ':
        return ' '

    input()


def play(f, mode=None):
    stage = load(f)
    init = State(stage)

    if mode is None:
        print("Load moves files? Please enter file name")
        filename = input("$>> ")

        if filename:
            pass
        else:
            input("Gaming mode, Ctrl+C to quit")

        s = init
        while True:
            print("\033[1H", end="")
            print("\033[J", end="")
            print(s)

            if s.isGoal():
                print("[+] You made {} moves".format(len(s.moves)))
                print("[+] Press to continue")
                click.getchar()
                break

            try:
                # key = get_key()
                # key = moves(int(input()))

                print("[+] Make a move")
                key = getKey()

                while key == ' ':
                    if not s.isSplit():
                        break
                    s.toggleActive()
                    print("\033[1H", end="")
                    print("\033[J", end="")
                    print(s)
                    key = getKey()

            except KeyboardInterrupt:
                break

            try:
                move(s, key)
            except Exception as e:
                print("--- Invalid move, revert\n--- {}".format(e))
                click.getchar()

    else:
        problem = Solver(init, mode)
        problem.solve()
        print(problem)
