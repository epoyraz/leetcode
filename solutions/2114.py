class Solution:
    def minSessions(self, tasks, sessionTime):
        n = len(tasks)
        memo = {}

        def dfs(mask, curr):
            key = (mask, curr)
            if key in memo:
                return memo[key]

            if mask == (1 << n) - 1:
                return 0 if curr == 0 else 1

            res = float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    t = tasks[i]
                    if curr + t <= sessionTime:
                        res = min(res, dfs(mask | (1 << i), curr + t))
                    else:
                        res = min(res, 1 + dfs(mask | (1 << i), t))

            memo[key] = res
            return res

        return dfs(0, 0)
