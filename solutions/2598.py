class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        res = float('inf')

        for i in range(n):
            if words[i] == target:
                dist = min(abs(i - startIndex), n - abs(i - startIndex))
                res = min(res, dist)

        return res if res != float('inf') else -1
