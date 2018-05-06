from copy import deepcopy
from bloxorz.common.moves import moves
from bloxorz.solver.State import move
from bloxorz.solver.State import getTrace

def DFS(s):
    stack = [s.queue.get()]
    setTrace = s.setTrace
    count = 0
    while len(stack) > 0:
        print("[+] Looping... {:5} / 50000".format(count), end='\r')
        if count > 50000:
            return False

        count += 1
        cur_state = stack[-1]
        stack.pop()

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
                        stack.append(new_state)
                        setTrace.add(new_trace)
                        # if step != 0:
                        # if cur_state.getSelectingBlock() != (numBlocks + 1):
                        #   new_state.moves.append(' ')
                        # new_state.moves.append(m)
                except Exception:
                    continue

    return False