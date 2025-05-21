import bisect

class Solution(object):
    def maximizeWin(self, prizePositions, k):
        n = len(prizePositions)
        left_max = [0] * (n + 1)
        res = 0

        j = 0
        for i in range(n):
            while prizePositions[i] - prizePositions[j] > k:
                j += 1
            win = i - j + 1
            left_max[i + 1] = max(left_max[i], win)

        j = n - 1
        for i in reversed(range(n)):
            while j >= 0 and prizePositions[j] - prizePositions[i] > k:
                j -= 1
            win = j - i + 1
            res = max(res, win + left_max[i])

        return res
