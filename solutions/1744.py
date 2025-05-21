class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        m = len(words[0])
        tlen = len(target)
        
        # 1) Build frequency table: freq[i][c] = count of char c at column i
        freq = [[0]*26 for _ in range(m)]
        for w in words:
            for i, ch in enumerate(w):
                freq[i][ord(ch)-97] += 1
        
        # 2) dp[j] = number of ways to form target[:j] so far
        dp = [0] * (tlen + 1)
        dp[0] = 1
        
        # 3) Process columns one by one
        for i in range(m):
            f = freq[i]
            # update dp from back to front so we don't reuse this column
            for j in range(tlen-1, -1, -1):
                c = ord(target[j]) - 97
                cnt = f[c]
                if cnt:
                    dp[j+1] = (dp[j+1] + dp[j] * cnt) % MOD
        
        return dp[tlen]
