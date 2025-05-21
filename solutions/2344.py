from collections import deque

class Solution:
    def maximumMinutes(self, grid):
        m, n = len(grid), len(grid[0])
        src, dst = (0,0), (m-1, n-1)
        
        def inb(r,c):
            return 0 <= r < m and 0 <= c < n
        
        # 1) fire_time BFS
        INF = 10**18
        fire_time = [[INF]*n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire_time[i][j] = 0
                    q.append((i,j,0))
                elif grid[i][j] == 2:
                    fire_time[i][j] = -1
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c,t = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if not inb(nr,nc) or grid[nr][nc]==2: continue
                if fire_time[nr][nc] > t+1:
                    fire_time[nr][nc] = t+1
                    q.append((nr,nc,t+1))
        
        # 2) plain reachability
        seen = [[False]*n for _ in range(m)]
        dq = deque([src])
        seen[0][0] = True
        reachable = False
        while dq:
            r,c = dq.popleft()
            if (r,c)==dst:
                reachable = True
                break
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if inb(nr,nc) and not seen[nr][nc] and grid[nr][nc]!=2:
                    seen[nr][nc] = True
                    dq.append((nr,nc))
        if not reachable:
            return -1
        
        # 3) infiniteâwait case
        if fire_time[dst[0]][dst[1]] == INF:
            return 10**9
        
        # 4) can_wait(T) with corrected stepping rule
        def can_wait(T):
            if T > fire_time[src[0]][src[1]]:
                return False
            vis = [[False]*n for _ in range(m)]
            dq = deque()
            vis[0][0] = True
            dq.append((0,0,T))
            
            while dq:
                r,c,t = dq.popleft()
                if (r,c)==dst and t <= fire_time[r][c]:
                    return True
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    nt = t+1
                    if (not inb(nr,nc) or vis[nr][nc] or grid[nr][nc]==2):
                        continue
                    # **strict** check: must have fire_time > nt, unless it's the dest
                    if nt >= fire_time[nr][nc] and (nr,nc) != dst:
                        continue
                    vis[nr][nc] = True
                    dq.append((nr,nc,nt))
            return False
        
        # 5) binaryâsearch T
        lo, hi = 0, fire_time[src[0]][src[1]]
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if can_wait(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        
        return ans
