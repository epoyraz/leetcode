from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        freq = Counter(nums)
        maxv = max(nums)
        points = [0] * (maxv + 1)
        for v, c in freq.items():
            points[v] = v * c

        prev2, prev1 = 0, points[0]
        for i in range(1, maxv + 1):
            curr = max(prev1, prev2 + points[i])
            prev2, prev1 = prev1, curr
        return prev1
