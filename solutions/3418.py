class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        # Count how many times each remainder mod 24 appears
        freq = [0]*24
        for h in hours:
            freq[h % 24] += 1

        # Pairs among remainder 0
        res = freq[0] * (freq[0] - 1) // 2

        # Pairs between r and 24-r for r = 1..11
        for r in range(1, 12):
            res += freq[r] * freq[24 - r]

        # Pairs among remainder 12 (since 12+12 = 24)
        res += freq[12] * (freq[12] - 1) // 2

        return res
