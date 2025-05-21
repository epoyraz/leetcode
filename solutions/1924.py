class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        zero = 0
        counts = [0] * batchSize
        for g in groups:
            r = g % batchSize
            if r == 0:
                zero += 1
            else:
                counts[r] += 1

        memo = {}
        def dfs(counts_tuple, curr_rem):
            key = (counts_tuple, curr_rem)
            if key in memo:
                return memo[key]
            counts_list = list(counts_tuple)
            if sum(counts_list) == 0:
                return 0
            best = 0
            for r in range(1, batchSize):
                if counts_list[r] > 0:
                    counts_list[r] -= 1
                    next_rem = (curr_rem + r) % batchSize
                    inc = 1 if curr_rem == 0 else 0
                    val = inc + dfs(tuple(counts_list), next_rem)
                    if val > best:
                        best = val
                    counts_list[r] += 1
            memo[key] = best
            return best

        return zero + dfs(tuple(counts), 0)
