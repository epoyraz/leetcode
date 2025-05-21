from collections import deque

class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        forbidden = set(forbidden)
        if x == 0:
            return 0
        
        # Upper bound on positions weâll consider
        limit = max(forbidden | {x}) + a + b
        
        # BFS queue: (position, last_was_backward)
        q = deque([(0, False)])
        visited = {(0, False)}
        
        jumps = 0
        while q:
            for _ in range(len(q)):
                pos, came_back = q.popleft()
                if pos == x:
                    return jumps
                
                # 1) Try forward jump
                fwd = pos + a
                if fwd <= limit and fwd not in forbidden and (fwd, False) not in visited:
                    visited.add((fwd, False))
                    q.append((fwd, False))
                
                # 2) Try backward jump (only if we didnât just come backward)
                if not came_back:
                    back = pos - b
                    if back >= 0 and back not in forbidden and (back, True) not in visited:
                        visited.add((back, True))
                        q.append((back, True))
            
            jumps += 1
        
        return -1
