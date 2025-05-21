class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        res = 0
        l, r = 0, len(piles) - 1
        for _ in range(n):
            # We take the triplet (piles[l], piles[r-1], piles[r])
            # Alice takes piles[r], we take piles[r-1], Bob takes piles[l]
            res += piles[r-1]
            l += 1
            r -= 2
        return res
