import sys
sys.setrecursionlimit(10**7)

# Ensure gcd compatibility
try:
    from math import gcd
except ImportError:
    from fractions import gcd

class Solution(object):
    def maxTravelScore(self, n, k, stayScore, travelScore):
        """
        :type n: int
        :type k: int
        :type stayScore: List[List[int]]
        :type travelScore: List[List[int]]
        :rtype: int
        """
        dp_prev = [0] * n
        for day in range(k):
            dp_cur = [0] * n
            for dest in range(n):
                stay = dp_prev[dest] + stayScore[day][dest]
                max_travel = max(dp_prev[p] + travelScore[p][dest] for p in range(n))
                dp_cur[dest] = max(stay, max_travel)
            dp_prev = dp_cur
        return max(dp_prev)

    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        mod = 10**9+7
        runs = []
        cur_char, cur_len = None, 0
        for c in word:
            if c == cur_char:
                cur_len += 1
            else:
                if cur_len:
                    runs.append(cur_len)
                cur_char, cur_len = c, 1
        if cur_len:
            runs.append(cur_len)
        m = len(runs)
        total = 1
        for Li in runs:
            total = total * Li % mod
        if m >= k:
            return total
        dp = [0] * k
        dp[0] = 1
        for Li in runs:
            prefix = [0] * k
            prefix[0] = dp[0]
            for i in range(1, k):
                prefix[i] = (prefix[i-1] + dp[i]) % mod
            new_dp = [0] * k
            for t_idx in range(1, k):
                a = prefix[t_idx-1]
                b = prefix[t_idx-1-Li] if t_idx-1-Li >= 0 else 0
                new_dp[t_idx] = (a - b) % mod
            dp = new_dp
        count_bad = sum(dp) % mod
        return (total - count_bad + mod) % mod

    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lcm(a, b):
            return a // gcd(a, b) * b

        n = len(nums)
        if n == 0:
            return 0

        prefix_g = [0] * n
        prefix_l = [0] * n
        suffix_g = [0] * n
        suffix_l = [0] * n

        for i in range(n):
            if i == 0:
                prefix_g[i] = nums[i]
                prefix_l[i] = nums[i]
            else:
                prefix_g[i] = gcd(prefix_g[i-1], nums[i])
                prefix_l[i] = lcm(prefix_l[i-1], nums[i])

        for i in range(n-1, -1, -1):
            if i == n-1:
                suffix_g[i] = nums[i]
                suffix_l[i] = nums[i]
            else:
                suffix_g[i] = gcd(suffix_g[i+1], nums[i])
                suffix_l[i] = lcm(suffix_l[i+1], nums[i])

        max_score = prefix_g[n-1] * prefix_l[n-1]

        for i in range(n):
            if n == 1:
                continue
            if i == 0:
                g = suffix_g[1]
                l = suffix_l[1]
            elif i == n-1:
                g = prefix_g[n-2]
                l = prefix_l[n-2]
            else:
                g = gcd(prefix_g[i-1], suffix_g[i+1])
                l = lcm(prefix_l[i-1], suffix_l[i+1])
            max_score = max(max_score, g * l)

        return max_score

    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [1] * 26
        for _ in range(t):
            new_dp = [0] * 26
            for i in range(25):
                new_dp[i] = dp[i+1]
            new_dp[25] = (dp[0] + dp[1]) % mod
            dp = new_dp
        result = 0
        for ch in s:
            result = (result + dp[ord(ch) - ord('a')]) % mod
        return result

    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9+7
        n = len(nums)
        maxv = max(nums) if nums else 0
        # Precompute gcd table
        gcd_table = [[0] * (maxv+1) for _ in range(maxv+1)]
        for i in range(maxv+1):
            for j in range(maxv+1):
                gcd_table[i][j] = gcd(i, j)
        # dp[g1][g2]: number of ways so far with gcd(seq1)=g1, gcd(seq2)=g2
        dp = [[0] * (maxv+1) for _ in range(maxv+1)]
        dp[0][0] = 1
        for x in nums:
            new_dp = [[0] * (maxv+1) for _ in range(maxv+1)]
            for g1 in range(maxv+1):
                for g2 in range(maxv+1):
                    ways = dp[g1][g2]
                    if ways == 0: continue
                    # skip x
                    new_dp[g1][g2] = (new_dp[g1][g2] + ways) % mod
                    # put in seq1
                    ng1 = x if g1 == 0 else gcd_table[g1][x]
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + ways) % mod
                    # put in seq2
                    ng2 = x if g2 == 0 else gcd_table[g2][x]
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + ways) % mod
            dp = new_dp
        # count pairs with equal non-zero gcd
        result = 0
        for g in range(1, maxv+1):
            result = (result + dp[g][g]) % mod
        return result