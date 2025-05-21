from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque([("0000", 0)])
        visited = set("0000")
        
        while queue:
            node, step = queue.popleft()
            if node == target:
                return step
            for i in range(4):
                for move in (-1, 1):
                    nxt = node[:i] + str((int(node[i]) + move) % 10) + node[i+1:]
                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, step + 1))
        return -1
