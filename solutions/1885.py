class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        total = 0
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                total += count * (count + 1) // 2
                count = 1

        # Add the last group
        total += count * (count + 1) // 2
        return total % MOD
