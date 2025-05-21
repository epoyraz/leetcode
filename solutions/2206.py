from collections import deque

class Solution:
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        # Build graph: edge i->j if bomb j is within range of bomb i
        adj = [[] for _ in range(n)]
        for i in range(n):
            x_i, y_i, r_i = bombs[i]
            r2 = r_i * r_i
            for j in range(n):
                if i == j:
                    continue
                x_j, y_j, _ = bombs[j]
                dx = x_j - x_i
                dy = y_j - y_i
                if dx*dx + dy*dy <= r2:
                    adj[i].append(j)
        
        def bfs(start):
            # Count how many bombs can be detonated starting from 'start'
            seen = {start}
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            return len(seen)
        
        # Try detonating each bomb and take the maximum reach
        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        
        return ans
