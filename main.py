from bloxorz.stages.GenStage import GenStage
from bloxorz.game.play import play


if __name__ == "__main__":
    while True:
        print("1. Generate stages")
        print("2. Play stage")
        print("3. Exit")

        try:
            choice = int(input("$>> "))
        except ValueError:
            print("--- A number is required")
            exit(-1)

        if choice == 3:
            exit(0)

        if choice == 1:
            GenStage()
            continue

        try:
            print("Choose your favorite stage")
            print("0 to play all game")
            choice = int(input("$>> "))
        except ValueError:
            print("--- A number is required")
            exit(-1)

        if choice > 33 or choice < 0:
            print("No such level")
            exit(-2)
        elif choice == 0:
            pass
        else:
            play("stage{}".format(choice))
