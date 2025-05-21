class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)
        # 1) Basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > n - max(i, j):
                    return ""
        
        # 2) Greedily build the lexicographically smallest string
        res = []
        for i in range(n):
            # start with all lowercase letters
            possible = set(chr(ord('a') + k) for k in range(26))
            for j in range(i):
                if lcp[i][j] > 0:
                    # must match res[j]
                    possible &= {res[j]}
                else:
                    # must differ from res[j]
                    possible.discard(res[j])
                if not possible:
                    return ""
            # pick smallest letter
            c = min(possible)
            res.append(c)
        word = "".join(res)
        
        # 3) Recompute LCP to verify
        lcp2 = [[0]*n for _ in range(n)]
        # fill from bottom-right up for easy DP
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i+1 < n and j+1 < n:
                        lcp2[i][j] = 1 + lcp2[i+1][j+1]
                    else:
                        lcp2[i][j] = 1
                else:
                    lcp2[i][j] = 0
        
        if lcp2 == lcp:
            return word
        else:
            return ""
