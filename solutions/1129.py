class Solution:
    def longestStrChain(self, words):
        words.sort(key=len)
        dp = {}
        res = 1
        for w in words:
            best = 1
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                if prev in dp:
                    best = max(best, dp[prev] + 1)
            dp[w] = best
            res = max(res, best)
        return res
