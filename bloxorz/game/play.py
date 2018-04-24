from bloxorz.stages.GenStage import GenStage
from bloxorz.solver.mode import mode as m
from bloxorz.solver.State import State, move
from bloxorz.solver.Solver import Solver
from bloxorz.common.getKey import getKey
from bloxorz.common.moves import moves, print_moves

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


def play(f, mode=None):
    stage = load(f)
    init = State(stage)

    if mode is None:
        """
        print("Load moves files? Please enter file name")
        filename = input("$>> ")

        if filename:
            pass
        else:
            input("Gaming mode, Ctrl+C to quit")
        """
        input("Welcome to stage: {}".format(init.name))

        s = init
        while True:
            print("\033[1H", end="")
            print("\033[J", end="")
            print(s)
            print_moves(s.moves)

            if s.isGoal():
                print("[+] You made {} moves".format(s.moves_made()))
                print("[+] Press to continue")
                click.getchar()
                break

            try:
                print("[+] Make a move")
                key = getKey()

                while key == ' ':
                    if not s.isSplit():
                        break
                    s.toggleActive()
                    print("\033[1H", end="")
                    print("\033[J", end="")
                    print(s)
                    print_moves(s.moves)
                    print("[+] Make a move")
                    key = getKey()

            except KeyboardInterrupt:
                key = input("Quit now? (y/n) ")
                if key == "y" or key == "Y":
                    break

            if not isinstance(key, moves):
                continue

            try:
                move(s, key)
            except Exception as e:
                print("--- Invalid move, revert\n--- {}".format(e))
                click.getchar()

    else:
        problem = Solver(init, mode)
        problem.solve()
        print(problem)

        k = input("Replay? (y/n) ")
        if k == "y" or k == "Y":
            print("Press right arrow to next move")
            print("If no move left, press enter to exit")
            click.getchar()
            problem.replay()
