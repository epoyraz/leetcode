class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        count = 0
        result = 0

        for char in s:
            if char == '1':
                count += 1
            else:
                result += count * (count + 1) // 2
                count = 0

        # Add the last group if it ends with '1'
        result += count * (count + 1) // 2
        return result % MOD
