class Solution(object):
    def countPalindromes(self, s):
        MOD = 10**9 + 7
        n = len(s)
        # build suffix pair counts
        suffixCount = [0] * 10
        suffixPair = [[0] * 10 for _ in range(10)]
        suffixPairs = [None] * n
        for i in range(n - 1, -1, -1):
            suffixPairs[i] = [row[:] for row in suffixPair]
            d = ord(s[i]) - ord('0')
            for b in range(10):
                suffixPair[d][b] += suffixCount[b]
            suffixCount[d] += 1
        # scan prefixes and accumulate answer
        prefixCount = [0] * 10
        prefixPair = [[0] * 10 for _ in range(10)]
        ans = 0
        for k in range(n):
            sp = suffixPairs[k]
            for a in range(10):
                row = prefixPair[a]
                for b in range(10):
                    if row[b] and sp[b][a]:
                        ans = (ans + row[b] * sp[b][a]) % MOD
            d = ord(s[k]) - ord('0')
            for a in range(10):
                prefixPair[a][d] += prefixCount[a]
            prefixCount[d] += 1
        return ans
