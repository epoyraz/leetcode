class Solution(object):
    def getResults(self, queries):
        # Find the maximum x in any query
        N = max(q[1] for q in queries)
        
        INF = 10**18
        size = 4*(N+1)
        left_obs  = [INF] * size
        right_obs = [-INF] * size
        max_gap   = [0]   * size
        
        def _combine(node, lnode, rnode):
            # combine child rnode into lnode, store in node
            left_obs[node]  = min(left_obs[lnode],  left_obs[rnode])
            right_obs[node] = max(right_obs[lnode], right_obs[rnode])
            # gap between the boundary obstacles of the two children
            bridge = 0
            if right_obs[lnode] != -INF and left_obs[rnode] != INF:
                bridge = left_obs[rnode] - right_obs[lnode]
            max_gap[node] = max(max_gap[lnode],
                               max_gap[rnode],
                               bridge)
        
        # Point-update: insert obstacle at position pos
        def update(node, l, r, pos):
            if l == r:
                left_obs[node] = right_obs[node] = pos
                max_gap[node] = 0
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(node*2,   l,    mid, pos)
            else:
                update(node*2+1, mid+1, r,   pos)
            _combine(node, node*2, node*2+1)
        
        # Range-query on [L..R], returning (left_obs, right_obs, max_gap)
        def query(node, l, r, L, R):
            if R < l or r < L:
                # no overlap
                return (INF, -INF, 0)
            if L <= l and r <= R:
                return (left_obs[node],
                        right_obs[node],
                        max_gap[node])
            mid = (l + r) // 2
            lo1, ro1, g1 = query(node*2,   l,    mid, L, R)
            lo2, ro2, g2 = query(node*2+1, mid+1, r,   L, R)
            # combine the two halves
            lo = min(lo1, lo2)
            ro = max(ro1, ro2)
            bridge = 0
            if ro1 != -INF and lo2 != INF:
                bridge = lo2 - ro1
            return (lo, ro, max(g1, g2, bridge))
        
        result = []
        for q in queries:
            if q[0] == 1:
                # place an obstacle
                x = q[1]
                update(1, 1, N, x)
            else:
                # can we fit a block of size sz in [0..x]?
                x, sz = q[1], q[2]
                lo, ro, g = query(1, 1, N, 1, x)
                # gap from 0 to first obstacle
                left_gap  = lo if lo != INF else x
                # gap from last obstacle to x
                right_gap = (x - ro) if ro != -INF else x
                max_free  = max(left_gap, right_gap, g)
                result.append(max_free >= sz)
        
        return result
