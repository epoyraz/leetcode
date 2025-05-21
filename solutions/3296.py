class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        # Compute Z-array
        Z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and word[Z[i]] == word[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1

        # t_max = ceil(n / k)
        t_max = (n + k - 1) // k
        for t in range(1, t_max + 1):
            d = t * k
            # if we've shifted out the whole string or more, we can rebuild arbitrarily
            if d >= n:
                return t
            # else, check whether suffix at d matches prefix of length n-d
            if Z[d] >= n - d:
                return t

        # Fallback (shouldn't happen)
        return t_max
