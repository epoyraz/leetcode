class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        memo = {}

        def dfs(used, total):
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                if not (used >> i) & 1:
                    if total + i >= desiredTotal or not dfs(used | (1 << i), total + i):
                        memo[used] = True
                        return True
            memo[used] = False
            return False

        return dfs(0, 0)
