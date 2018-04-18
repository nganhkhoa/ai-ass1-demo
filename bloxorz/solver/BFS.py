from bloxorz.solver.moves import moves
from queue import Queue

def BFS(s):
    print("[+] Looping...")
    q = queue.Queue()
    start_block = Block(1, 1)
    start_path = [board]
    start_node = Node(start_path, start_block)
    q.put(start_node)
    while not q.empty():
        top = q.get()
        if top.block.location[0] == goal[0] and top.block.location[1] == goal[
            1] and top.block.state == State.standingBlock:
            for i in range(len(top.path)):
                print(top.path[i])
            break
        block = top.block
        m = top.path[-1]
        if block.can_move_left(m):
            t = list(m)
            b = copy.deepcopy(block)
            b.move_left(t)
            p = list(top.path).append(t)
            temp = Node(p, b)
        if block.can_move_right(m):
            t = list(m)
            b = copy.deepcopy(block)
            b.move_right(t)
            p = list(top.path).append(t)
            temp = Node(p, b)
        if block.can_move_up(m):
            t = list(m)
            b = copy.deepcopy(block)
            b.move_up(t)
            p = list(top.path).append(t)
            temp = Node(p, b)
        if block.can_move_down(m):
            t = list(m)
            b = copy.deepcopy(block)
            b.move_down(t)
            p = list(top.path).append(t)
            temp = Node(p, b)
