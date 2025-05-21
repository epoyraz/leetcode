class Solution:
    def minDifference(self, nums, queries):
        n = len(nums)
        prefix = [[0] * 101 for _ in range(n + 1)]

        # Build prefix frequency table
        for i in range(n):
            for j in range(1, 101):
                prefix[i + 1][j] = prefix[i][j]
            prefix[i + 1][nums[i]] += 1

        res = []

        for l, r in queries:
            last = -1
            ans = float('inf')
            for x in range(1, 101):
                freq = prefix[r + 1][x] - prefix[l][x]
                if freq > 0:
                    if last != -1:
                        ans = min(ans, x - last)
                    last = x
            res.append(ans if ans != float('inf') else -1)

        return res
