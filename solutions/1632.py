class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left_count = [0] * n
        right_count = [0] * n

        seen_left = set()
        for i in range(n):
            seen_left.add(s[i])
            left_count[i] = len(seen_left)

        seen_right = set()
        for i in range(n - 1, -1, -1):
            seen_right.add(s[i])
            right_count[i] = len(seen_right)

        res = 0
        for i in range(n - 1):
            if left_count[i] == right_count[i + 1]:
                res += 1

        return res
