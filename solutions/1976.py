class Solution:
    def splitString(self, s):
        def dfs(prev, i, cnt):
            if i == len(s):
                return cnt >= 2
            num = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if prev is None or prev - num == 1:
                    if dfs(num, j + 1, cnt + 1):
                        return True
                if prev is not None and num >= prev:
                    break
            return False
        return dfs(None, 0, 0)
