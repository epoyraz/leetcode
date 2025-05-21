from collections import deque

class Solution:
    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        
        # Convert initial matrix to a bitmask integer
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)
        
        # Directions: up, down, left, right, center
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

        def flip(state, x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    pos = nx * n + ny
                    state ^= (1 << pos)
            return state

        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        while queue:
            state, steps = queue.popleft()
            if state == 0:
                return steps
            for i in range(m):
                for j in range(n):
                    new_state = flip(state, i, j)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))

        return -1
