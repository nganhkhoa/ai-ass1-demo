from bloxorz.common.getKey import getKey
from bloxorz.common.moves import moves


def menu(title, selections, choice=1):
    while True:
        print("\033[1H", end="")
        print("\033[J", end="")
        print(title)

        for i in range(len(selections)):
            if i == choice - 1:
                print("\033[1;91m> ", end="")
            print("{}. ".format(i + 1), end="")
            print(selections[i])
            if i == choice - 1:
                print("\033[0m", end="")

        key = getKey()

        if key == moves.up:
            choice = (choice - 2) % len(selections) + 1
        elif key == moves.down:
            choice = (choice) % len(selections) + 1
        elif key == '\n':
            return choice
        else:
            continue

        # if selection == 0:
        #     selection = len(selections)
        # if selection > len(selections):
        #     selection = 1