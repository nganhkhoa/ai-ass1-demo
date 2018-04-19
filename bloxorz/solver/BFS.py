from bloxorz.solver.moves import moves
from bloxorz.solver.State import move
from queue import Queue
from copy import deepcopy

def BFS(s):
    queue = s.queue

    loop = 1
    while len(queue) != 0 and loop <= 50000:
        try:
            print("[+] Looping {:5d} / {}".format(loop, 50000), end='\r')
            loop += 1

            state = queue[0]
            queue = queue[1:]

            if loop != 2:
                # stop go back to begin
                if state.isBegin():
                    continue

            try:
                if state.isSplit():
                    new_states = [deepcopy(state) for i in range(8)]
                else:
                    new_states = [deepcopy(state) for i in range(4)]
                # print("[+] Deep copied")
            except KeyboardInterrupt:
                print("\nDeep coping from:")
                print("Ctrl+C again to break")
                try:
                    input(state)
                except KeyboardInterrupt:
                    break
                print("\033[1H", end="")
                print("\033[J", end="")

            for active in range(2 if state.isSplit() else 1):
                for i in range(4):
                    try:
                        new_states[i + 4 * active].setActiveBlock(active + 1)
                        m = moves(i + 1)
                        try:
                            # don't make a reverse move
                            if m.isReverse(new_states[i].moves[-1]):
                                # print("{} reverse {}".format(m, new_states[i].moves[-1]))
                                continue
                        except IndexError:
                            # first loop has no moves
                            pass
                        move(new_states[i], m)
                        print(m)
                        print(new_states[i])

                        # check already have

                        if new_states[i].isGoal():
                            s.goal = new_states[i]
                            print()
                            return

                    except KeyboardInterrupt:
                        print("\nChecking state:")
                        input(new_states[i])
                        print("\033[1H", end="")
                        print("\033[J", end="")

                    except Exception:
                        # invalid move
                        continue

                    queue.append(new_states[i])

        except KeyboardInterrupt:
            print("\nInterupted in unexpected code")
            input("Sometimes this happens, try breaking again")
            print("\033[1H", end="")
            print("\033[J", end="")