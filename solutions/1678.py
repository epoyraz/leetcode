class Solution(object):
    def numWays(self, s):
        mod = 10**9 + 7
        n = len(s)
        total_ones = s.count('1')
        if total_ones % 3 != 0:
            return 0
        if total_ones == 0:
            # choose any two split points among n-1 gaps
            return ((n-1) * (n-2) // 2) % mod
        k = total_ones // 3
        ones = [i for i, ch in enumerate(s) if ch == '1']
        # gaps after k-th and 2k-th ones
        a = ones[k] - ones[k-1]
        b = ones[2*k] - ones[2*k-1]
        return (a * b) % mod
