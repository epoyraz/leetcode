class Solution(object):
    def substringXorQueries(self, s, queries):
        n = len(s)
        best = {}
        MAX_LEN = 32  # enough to cover up to 2^31 values
        
        # Precompute the best (shortest, then leftmost) substring for every value
        for i in xrange(n):
            val = 0
            for l in xrange(1, MAX_LEN + 1):
                j = i + l - 1
                if j >= n:
                    break
                # build the integer value of s[i..j]
                val = (val << 1) + (ord(s[j]) - ord('0'))
                # record if this is the first time we see val, or it's a shorter
                # substring, or same length but more leftmost
                if val not in best or l < best[val][0] or (l == best[val][0] and i < best[val][1]):
                    best[val] = (l, i, j)
        
        # Answer the queries
        ans = []
        for first, second in queries:
            target = first ^ second
            if target in best:
                _, left, right = best[target]
                ans.append([left, right])
            else:
                ans.append([-1, -1])
        return ans
