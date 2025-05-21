class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        # No adjacent pairs at all if length < 2
        if n <= 1:
            return 0

        # map each letter to 0..25
        w = [ord(c) - ord('a') for c in word]
        INF = 10**9

        # dp[i][c] = min changes to fix word[0..i] ending with char c
        dp = [[INF]*26 for _ in range(n)]

        # base case i = 0
        for c in range(26):
            dp[0][c] = (c != w[0])

        # transitions
        for i in range(1, n):
            for c in range(26):
                cost = (c != w[i])
                best = INF
                for p in range(26):
                    if abs(c - p) >= 2:
                        best = min(best, dp[i-1][p])
                dp[i][c] = best + cost

        # take the minimum over all endings
        return int(min(dp[n-1]))
