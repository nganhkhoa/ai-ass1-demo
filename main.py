from bloxorz.stages.GenStage import GenStage
from bloxorz.game.play import play
from bloxorz.solver.mode import mode as m
from bloxorz.common.getKey import getKey
from bloxorz.common.moves import moves
from bloxorz.common.menu import menu



def auto_play():
    try:
        print("\033[1H", end="")
        print("\033[J", end="")
        print("Choose your favorite stage")
        print("0 to play all game")
        choice = int(input("$>> "))
    except ValueError:
        print("--- A number is required")
        exit(-1)

    if choice > 33 or choice < 0:
        print("--- No such level {}".format(choice))
        exit(-2)
    elif choice == 0:
        pass
    else:
        choice = menu("Choose your algorithm\n! as not complete",
                    ["BFS (!)",
                    "DFS (!)",
                    "Hill clibming (!)",
                    "Simulated Annealing (!)",
                    "Best First Search (!)"])

        mode = m(int(choice))
        play("stage{}".format(choice), mode)
        input()


def manual_play():
    try:
        print("\033[1H", end="")
        print("\033[J", end="")
        print("Choose your favorite stage")
        print("0 to play all game")
        choice = int(input("$>> "))
    except ValueError:
        print("--- A number is required")
        exit(-1)

    if choice > 33 or choice < 0:
        print("--- No such level {}".format(choice))
        exit(-2)
    elif choice == 0:
        pass
    else:
        play("stage{}".format(choice))


if __name__ == "__main__":
    while (True):
        choice = menu("Welcome to Bloxorz",
                    ["Generate Stages",
                    "AI Play",
                    "Manual Play",
                    "Exit"])

        if choice == 4:
            exit()

        if choice == 1:
            GenStage()
            input()

        elif choice == 2:
            auto_play()
        
        elif choice == 3:
            manual_play()