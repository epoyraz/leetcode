from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        target = "123450"
        start = ''.join(str(c) for row in board for c in row)
        
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            state, step = queue.popleft()
            if state == target:
                return step
            idx = state.index('0')
            for nei in neighbors[idx]:
                lst = list(state)
                lst[idx], lst[nei] = lst[nei], lst[idx]
                new_state = ''.join(lst)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, step + 1))
        
        return -1
