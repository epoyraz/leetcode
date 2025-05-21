class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        # collect all the 1-cells
        ones = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]
        
        INF = 10**18
        ans = INF
        
        def eval_partition(assign_region):
            """
            assign_region(r,c) -> 0,1,2  says which of the 3 regions this cell belongs to.
            We scan all 1-cells, build bounding boxes for regions 0/1/2,
            and if each is non-empty, return sum of their areas, else INF.
            """
            # init mins/maxs
            min_r = [n, n, n]
            max_r = [-1, -1, -1]
            min_c = [m, m, m]
            max_c = [-1, -1, -1]
            cnt   = [0, 0, 0]
            for (r, c) in ones:
                k = assign_region(r, c)
                if not (0 <= k < 3):
                    # this split doesn't cover that 1
                    return INF
                cnt[k] += 1
                if r < min_r[k]: min_r[k] = r
                if r > max_r[k]: max_r[k] = r
                if c < min_c[k]: min_c[k] = c
                if c > max_c[k]: max_c[k] = c
            
            # all 3 regions must have at least one 1
            if cnt[0] == 0 or cnt[1] == 0 or cnt[2] == 0:
                return INF
            
            total = 0
            for k in range(3):
                h = max_r[k] - min_r[k] + 1
                w = max_c[k] - min_c[k] + 1
                total += h * w
            return total
        
        # 1) vertical stripes
        for c1 in range(m-2):
            for c2 in range(c1+1, m-1):
                def reg_v(r, c, c1=c1, c2=c2):
                    if c <= c1:   return 0
                    elif c <= c2: return 1
                    else:         return 2
                ans = min(ans, eval_partition(reg_v))
        
        # 2) horizontal stripes
        for r1 in range(n-2):
            for r2 in range(r1+1, n-1):
                def reg_h(r, c, r1=r1, r2=r2):
                    if r <= r1:   return 0
                    elif r <= r2: return 1
                    else:         return 2
                ans = min(ans, eval_partition(reg_h))
        
        # 3) horizontal cut, then vertical on bottom half
        for r in range(n-1):
            for c in range(m-1):
                def reg_hv(r0, c0, r=r, c=c):
                    if r0 <= r:
                        return 0
                    else:
                        return 1 if c0 <= c else 2
                ans = min(ans, eval_partition(reg_hv))
        
        # 4) horizontal cut, then vertical on top half
        for r in range(n-1):
            for c in range(m-1):
                def reg_hv2(r0, c0, r=r, c=c):
                    if r0 > r:
                        return 0
                    else:
                        return 1 if c0 <= c else 2
                ans = min(ans, eval_partition(reg_hv2))
        
        # 5) vertical cut, then horizontal on right half
        for c in range(m-1):
            for r in range(n-1):
                def reg_vh(r0, c0, r=r, c=c):
                    if c0 <= c:
                        return 0
                    else:
                        return 1 if r0 <= r else 2
                ans = min(ans, eval_partition(reg_vh))
        
        # 6) vertical cut, then horizontal on left half
        for c in range(m-1):
            for r in range(n-1):
                def reg_vh2(r0, c0, r=r, c=c):
                    if c0 > c:
                        return 0
                    else:
                        return 1 if r0 <= r else 2
                ans = min(ans, eval_partition(reg_vh2))
        
        return ans
