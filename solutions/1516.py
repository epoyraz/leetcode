class Solution(object):
    def getHappyString(self, n, k):
        result = []

        def backtrack(path):
            if len(path) == n:
                result.append(path)
                return
            for ch in 'abc':
                if not path or path[-1] != ch:
                    backtrack(path + ch)

        backtrack("")
        return result[k - 1] if k <= len(result) else ""
