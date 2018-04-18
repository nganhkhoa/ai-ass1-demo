from bloxorz.stages.GenStage import GenStage
from bloxorz.game.play import play
from bloxorz.game.mode import mode as m

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
        print("\033[1H", end="")
        print("\033[J", end="")
        print("Choose your algorithm")
        print("1. BFS")
        print("2. DFS")
        print("3. Hill clibming")
        print("4. Simulated Annealing")
        print("5. Best First Search")
        mode = m(int(input("$>> ")))
        play("stage{}".format(choice), mode)


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
    while True:
        print("\033[1H", end="")
        print("\033[J", end="")
        print("1. Generate stages")
        print("2. Auto Play stage")
        print("3. Manual Play stage")
        print("4. Exit")

        try:
            choice = int(input("$>> "))
        except ValueError:
            print("--- A number is required")
            exit(-1)

        if choice == 4:
            print(":( See you again")
            exit(0)

        if choice == 1:
            GenStage()
            input()
            continue

        if choice == 2:
            auto_play()
            input()
            continue

        if choice == 3:
            manual_play()
            continue