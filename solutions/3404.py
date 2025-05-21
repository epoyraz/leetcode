class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # Step 1: for each column, compute cost_j[v] = #cells to change to make column=j all = v
        # and include a wildcard None at cost = m (change all cells to some other value)
        costs = []
        for j in range(n):
            freq = {}
            for i in range(m):
                x = grid[i][j]
                freq[x] = freq.get(x, 0) + 1
            cost_j = {v: m - cnt for v, cnt in freq.items()}
            cost_j[None] = m  # change all to some fresh value
            costs.append(cost_j)

        # Step 2: DP over columns: dp_prev[v] = best cost up to previous column ending with value v
        dp_prev = costs[0].copy()

        for j in range(1, n):
            # find the two best (cost, value) pairs in dp_prev
            best1 = (float('inf'), None)
            best2 = (float('inf'), None)
            for v, c in dp_prev.items():
                if c < best1[0]:
                    best2 = best1
                    best1 = (c, v)
                elif c < best2[0]:
                    best2 = (c, v)

            dp_curr = {}
            for v, add_cost in costs[j].items():
                # choose best from previous that isnât the same v
                prev_best_cost = best1[0] if best1[1] != v else best2[0]
                dp_curr[v] = add_cost + prev_best_cost
            dp_prev = dp_curr

        # The answer is the minimum over all ending values
        return min(dp_prev.values())
