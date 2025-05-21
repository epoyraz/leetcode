class Solution:
    def punishmentNumber(self, n):
        def can_partition(s, target):
            def dfs(i, total):
                if i == len(s):
                    return total == target
                for j in range(i + 1, len(s) + 1):
                    if dfs(j, total + int(s[i:j])):
                        return True
                return False
            return dfs(0, 0)

        res = 0
        for i in range(1, n + 1):
            sq = str(i * i)
            if can_partition(sq, i):
                res += i * i
        return res
