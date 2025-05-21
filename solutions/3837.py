from collections import deque, defaultdict

class Solution(object):
    def minMoves(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        # 1) Gather portal positions by letter
        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                ch = matrix[i][j]
                if 'A' <= ch <= 'Z':
                    portals[ch].append((i, j))
        
        # 2) Distances, -1 = unvisited
        dist = [[-1]*n for _ in range(m)]
        dist[0][0] = 0
        
        # 3) Track used portals
        used = {ch: False for ch in portals}
        
        # 4) 0-1 BFS
        dq = deque()
        dq.append((0,0))
        while dq:
            x,y = dq.popleft()
            d = dist[x][y]
            # If reached target
            if x==m-1 and y==n-1:
                return d
            
            # 4a) Teleport if letter and not yet used
            ch = matrix[x][y]
            if 'A' <= ch <= 'Z' and not used[ch]:
                for nx, ny in portals[ch]:
                    # teleport cost = 0
                    if dist[nx][ny] == -1 or dist[nx][ny] > d:
                        dist[nx][ny] = d
                        dq.appendleft((nx, ny))
                used[ch] = True  # only once
            
            # 4b) Regular moves
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    if dist[nx][ny] == -1 or dist[nx][ny] > d+1:
                        dist[nx][ny] = d+1
                        dq.append((nx, ny))
        
        # Unreachable
        return -1
