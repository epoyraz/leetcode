class Solution(object):
    def numberOfArrays(self, s, k):
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # base case: 1 way to parse empty string

        max_len = len(str(k))  # limit substring length based on k

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0  # no numbers can start with '0'
                continue
            num = 0
            for j in range(i, min(i + max_len, n)):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD

        return dp[0]
