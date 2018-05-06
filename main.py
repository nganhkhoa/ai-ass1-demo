from bloxorz.stages.GenStage import GenStage
from bloxorz.game.play import play
from bloxorz.solver.mode import mode as m
from bloxorz.common.getKey import getKey
from bloxorz.common.moves import moves
from bloxorz.common.menu import menu

import colorama


def auto_play():
    try:
        print("\033[1H", end="")
        print("\033[J", end="")
        print("Choose your favorite stage")
        print("0 to play all game")
        choice = int(input("$>> "))
    except ValueError:
        input("--- A number is required")
        return

    if choice > 33 or choice < 0:
        input("--- No such level {}".format(choice))
        return

    mode = m(menu("Choose your algorithm\n! as not complete",
                ["BFS",
                "DFS",
                "Hill clibming (!)",
                "Simulated Annealing (!)",
                "Best First Search (!)"]))

    auto_replay = menu("Auto replay?", ["Yes", "No", "Ask me"], 1)
    if choice != 0:
        auto_next = menu("Auto next level?", ["Yes", "No", "Ask me"], 1)

    if choice != 0:
        while True:
            play("{}".format(choice), mode, auto_replay)
            if choice + 1 > 33 or auto_next == 2:
                break
            if auto_next == 1:
                choice += 1
                continue
            k = input("Next level? (y/n) ")
            if k != "y" and k != "Y":
                break
            choice += 1

    else:
        for i in range(33):
            play("{}".format(i + 1), mode, auto_replay)
        input()


def manual_play():
    try:
        print("\033[1H", end="")
        print("\033[J", end="")
        print("Choose your favorite stage")
        print("0 to play all game")
        choice = int(input("$>> "))
    except ValueError:
        input("--- A number is required")
        return

    if choice > 33 or choice < 0:
        input("--- No such level {}".format(choice))
        return
    elif choice == 0:
        for i in range(33):
            play("{}".format(i + 1))
    else:
        play("{}".format(choice))


if __name__ == "__main__":
    colorama.init()
    choice = 1

    with open('stat.csv', 'w') as f:
        f.write('mode,stage,time(s)\n')
        f.close()

    while (True):
        choice = menu("Welcome to Bloxorz",
                    ["Generate Stages",
                    "AI Play",
                    "Manual Play",
                    "Exit"], choice)

        if choice == 4:
            exit()

        elif choice == 1:
            GenStage()
            input()

        elif choice == 2:
            auto_play()
        
        elif choice == 3:
            manual_play()