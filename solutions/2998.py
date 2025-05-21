class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        cnt = 0
        for x in range(low, high + 1):
            s = str(x)
            L = len(s)
            if L % 2 != 0:
                continue
            half = L // 2
            if sum(int(c) for c in s[:half]) == sum(int(c) for c in s[half:]):
                cnt += 1
        return cnt
