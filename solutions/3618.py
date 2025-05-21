import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def maxScore(self, n, k, stayScore, travelScore):
        """
        :type n: int
        :type k: int
        :type stayScore: List[List[int]]
        :type travelScore: List[List[int]]
        :rtype: int
        """
        mod = 10**9+7
        # dp_prev[j] will hold the max score ending at city j after previous day
        dp_prev = [0] * n
        # Iterate over each day
        for day in range(k):
            dp_cur = [0] * n
            # Compute dp for current day
            for dest in range(n):
                # Option 1: stay in city dest
                stay = dp_prev[dest] + stayScore[day][dest]
                # Option 2: travel from some city p to dest
                # Initialize with travel from city 0
                max_travel = dp_prev[0] + travelScore[0][dest]
                # Check travel from other cities
                for p in range(1, n):
                    val = dp_prev[p] + travelScore[p][dest]
                    if val > max_travel:
                        max_travel = val
                # Choose the better option
                dp_cur[dest] = stay if stay > max_travel else max_travel
            dp_prev = dp_cur
        # The answer is the best score among all cities after k days
        return max(dp_prev)

    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        mod = 10**9+7
        # Compute run-lengths of the observed word
        runs = []
        cur_char = None
        cur_len = 0
        for c in word:
            if c == cur_char:
                cur_len += 1
            else:
                if cur_len > 0:
                    runs.append(cur_len)
                cur_char = c
                cur_len = 1
        if cur_len > 0:
            runs.append(cur_len)
        m = len(runs)
        # Total number of raw assignments (each run i has Li choices for Mi)
        total = 1
        for Li in runs:
            total = (total * Li) % mod
        # If minimum possible original length m >= k, all assignments are valid
        if m >= k:
            return total
        # Otherwise, subtract those with sum Mi < k via DP up to k-1
        dp = [0] * k
        dp[0] = 1
        for Li in runs:
            # Compute prefix sums of dp
            prefix = [0] * k
            prefix[0] = dp[0]
            for i in range(1, k):
                prefix[i] = (prefix[i-1] + dp[i]) % mod
            new_dp = [0] * k
            # For each possible total t (<k), count assignments ending at t
            for t in range(1, k):
                a = prefix[t-1]
                b = prefix[t-1-Li] if t-1-Li >= 0 else 0
                new_dp[t] = (a - b) % mod
            dp = new_dp
        # Count of assignments with sum Mi < k is sum(dp[0..k-1])
        count_bad = sum(dp) % mod
        return (total - count_bad + mod) % mod
