class Solution(object):
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        ans = 0
        
        while True:
            regions = []
            frontiers = []
            walls = []
            visited = [[0] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        region = []
                        frontier = set()
                        wall = 0
                        stack = [(i, j)]
                        visited[i][j] = 1
                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))
                            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        wall += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = 1
                                        stack.append((nx, ny))
                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall)
            
            if not regions:
                break
            
            idx = frontiers.index(max(frontiers, key=len))
            ans += walls[idx]
            
            for i, region in enumerate(regions):
                if i == idx:
                    for x, y in region:
                        isInfected[x][y] = -1
                else:
                    for x, y in frontiers[i]:
                        isInfected[x][y] = 1
                        
        return ans
