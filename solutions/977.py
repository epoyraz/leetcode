class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # empty subsequence

        last = {}  # last occurrence index of each character

        for i in range(len(s)):
            char = s[i]
            dp[i + 1] = (dp[i] * 2) % MOD
            if char in last:
                dp[i + 1] = (dp[i + 1] - dp[last[char]]) % MOD
            last[char] = i

        # subtract the empty subsequence
        return (dp[len(s)] - 1) % MOD
