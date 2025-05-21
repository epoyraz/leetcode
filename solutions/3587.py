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