from bloxorz.common.moves import moves
from bloxorz.solver.State import move
from bloxorz.solver.State import getTrace

from queue import Queue
from copy import deepcopy

"""
# s is a solver(queue, mode, goal)
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

"""


# s is a solver(queue, mode, goal)
def BFS(s):
    queue = s.queue
    setTrace = s.setTrace
    count = 0
    while not queue.empty():
        print("[+] Looping... {:5} / 50000".format(count), end='\r')
        if count > 50000:
            return False

        count += 1
        cur_state = queue.get()

        if cur_state.isGoal():
            s.goal = cur_state
            print('[+] I have found the solution after {} iterations'.format(count))
            return True

        for numBlocks in range(2 if cur_state.isSplit() else 1):
            # for each block in blox
            for step in range(0 if cur_state.isSplit() else 1, 5):
                # up down left right
                try:
                    new_state = deepcopy(cur_state)
                    new_state.setActiveBlock(numBlocks + 1)
                    m = moves(step)
                    move(new_state, m)
                    new_trace = getTrace(new_state.getBoard(), new_state.blox)
                    # print(new_trace)
                    if new_trace not in setTrace:
                        # print(new_state)
                        queue.put(new_state)
                        setTrace.add(new_trace)
                        #if step != 0:
                            #if cur_state.getSelectingBlock() != (numBlocks + 1):
                             #   new_state.moves.append(' ')
                            #new_state.moves.append(m)
                except Exception:
                    continue

    return False