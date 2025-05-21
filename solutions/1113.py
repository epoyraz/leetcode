class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)

        # -------- maximum moves ----------
        max_moves = max(stones[-1] - stones[1], stones[-2] - stones[0]) - (n - 2)

        # -------- minimum moves ----------
        min_moves = n
        i = 0
        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1
            window = j - i + 1
            min_moves = min(min_moves, n - window)

        # special case: all stones are consecutive except one gap of size 2
        if (stones[-2] - stones[0] == n - 2 and stones[-1] - stones[-2] > 2) or \
           (stones[-1] - stones[1] == n - 2 and stones[1] - stones[0] > 2):
            min_moves = 2

        return [min_moves, max_moves]
