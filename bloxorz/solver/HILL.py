from copy import deepcopy
from bloxorz.common.moves import moves
from bloxorz.solver.State import move
from bloxorz.solver.State import getTrace

def EVAL(state):
    ans = None
    # implement code here
    
    return ans

def HILL(s):
    setTrace = s.setTrace
    count = 0
    prevEval = None
    cur_state = s.init
    while 1:
        print("[+] Looping... {:5} / 50000".format(count), end='\r')
        if count > 50000:
            return False

        count += 1

        if cur_state.isGoal():
            s.goal = cur_state
            print('[+] I have found the solution after {} iterations'.format(count))
            return True
        
        cannotMove = [True, True] if cur_state.isSplit() else [True]

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
                    newEval = EVAL(new_state)
                    if new_trace not in setTrace and newEval < prevEval:
                        prevEval = newEval
                        cur_state = new_state
                        setTrace.add(new_trace)
                        cannotMove[numBlocks] = False
                        break
            
                except Exception:
                    continue
        
        if cannotMove[0] is True:
            if cur_state.isSplit():
                if cannotMove[1] is True:
                    return False
            else:
                return False

    return False
