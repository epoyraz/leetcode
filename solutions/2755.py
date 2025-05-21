class Solution:
    def minExtraChar(self, s, dictionary):
        n = len(s)
        word_set = set(dictionary)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1  # assume s[i] is extra
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])
        return dp[0]
