class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        # 1) Coordinateâcompress x and y separately
        xs = sorted({x for x, _ in points})
        ys = sorted({y for _, y in points})
        map_x = {x:i for i, x in enumerate(xs)}
        map_y = {y:i for i, y in enumerate(ys)}
        nx, ny = len(xs), len(ys)
        
        # 2) Build the occupancy grid G
        G = [[0]*ny for _ in range(nx)]
        comp = [None]*n
        for idx, (x, y) in enumerate(points):
            cx = map_x[x]
            cy = map_y[y]
            G[cx][cy] = 1
            comp[idx] = (cx, cy)
        
        # 3) Build 2D prefixâsum P over G
        #    P[i+1][j+1] = sum of G[0..i][0..j]
        P = [[0]*(ny+1) for _ in range(nx+1)]
        for i in range(nx):
            row_sum = 0
            for j in range(ny):
                row_sum += G[i][j]
                P[i+1][j+1] = P[i][j+1] + row_sum
        
        # 4) Count all ordered pairs (i->Alice, j->Bob)
        ans = 0
        for i in range(n):
            xi, yi = comp[i]
            for j in range(n):
                xj, yj = comp[j]
                # Alice at i must be upperâleft of Bob at j
                if xi <= xj and yi >= yj:
                    # query how many points in the inclusive rectangle [xi..xj] x [yj..yi]
                    cnt = (
                        P[xj+1][yi+1]
                        - P[xi][yi+1]
                        - P[xj+1][yj]
                        + P[xi][yj]
                    )
                    # if exactly those two, it's empty
                    if cnt == 2:
                        ans += 1
        
        return ans
