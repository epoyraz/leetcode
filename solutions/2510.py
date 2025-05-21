class Solution(object):
    def deleteString(self, s):
        n = len(s)
        # 1) Build LCP table in O(n^2):
        #    lcp[i][j] = length of longest common prefix of s[i:] and s[j:]
        lcp = [ [0]*n for _ in range(n) ]
        for i in range(n-1, -1, -1):
            si = s[i]
            row_i = lcp[i]
            for j in range(n-1, i, -1):
                if si == s[j]:
                    row_i[j] = 1 + (lcp[i+1][j+1] if j+1<n else 0)

        # 2) dp[i] = max ops to delete s[i:]
        dp = [0]*(n+1)
        # dp[n] = 0 by default
        for i in range(n-1, -1, -1):
            best = 1  # you can always delete the entire suffix
            limit = (n - i) // 2
            li = lcp[i]
            dpi = dp  # local alias
            for ell in range(1, limit+1):
                # if first ell chars == next ell chars
                if li[i+ell] >= ell:
                    val = 1 + dpi[i+ell]
                    if val > best:
                        best = val
            dp[i] = best

        return dp[0]
