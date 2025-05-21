class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        freq = [0] * 24
        count = 0
        for h in hours:
            r = h % 24
            c = (-r) % 24            # the remainder needed to make (r + c) â¡ 0 mod 24
            count += freq[c]
            freq[r] += 1
        return count
