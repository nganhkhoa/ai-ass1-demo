from copy import deepcopy
from bloxorz.common.moves import moves
from bloxorz.solver.State import move
from bloxorz.solver.State import getTrace


class pair:
    def __init__(self, state, value):
        self.state = state
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False


# location 1 is our block, location 2 is goal
def distance(location1, location2):
    return abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])


def EVAL(state, goal):
    ans = 0
    for numBlocks in range(2 if state.isSplit() else 1):
        ans += distance(state.blox[numBlocks].getIndex(), goal)
    return ans


def HILL(s):
    setTrace = s.setTrace
    count = 0
    state = s.queue.get()
    goal = None
    for line in state.board:
        for tile in line:
            if tile is not None and tile.isGoal():
               goal = [state.board.index(line), line.index(tile)]
    stack = [state]
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

        priority = []
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
                    newEval = EVAL(new_state, goal)
                    if new_trace not in setTrace:
                        priority.append(pair(new_state, newEval))
                        setTrace.add(new_trace)
                except Exception:
                    continue
        priority.sort(reverse = True)
        for i in range(len(priority)):
            stack.append(priority[i].state)

    return False
