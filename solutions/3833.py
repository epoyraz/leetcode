class Solution(object):
    def minTravelTime(self, l, n, k, position, time):
        """
        :type l: int
        :type n: int
        :type k: int
        :type position: List[int]
        :type time: List[int]
        :rtype: int
        """
        # Prefix sums of original time array
        # pref[i] = sum of time[0] through time[i-1]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + time[i]

        # dp[i][j] is a dict mapping effective travel-time-per-km at sign i
        # to the min total cost to reach i using exactly j merges.
        dp = [[{} for _ in range(k + 1)] for _ in range(n)]
        # Initialize at start sign (index 0)
        # No merges used, effective time at sign 0 is the original time[0]
        dp[0][0][time[0]] = 0

        # Fill DP
        for i in range(n):
            for used in range(k + 1):
                for eff_t, cost_so_far in dp[i][used].items():
                    # Try jumping to any next kept sign h > i
                    for h in range(i + 1, n):
                        merges_needed = h - i - 1
                        if used + merges_needed > k:
                            continue
                        # Travel cost for segment from i to h using current eff_t
                        dist = position[h] - position[i]
                        new_cost = cost_so_far + dist * eff_t
                        # Compute new effective time at sign h after merging
                        # interior signs i+1 .. h-1 into h
                        new_eff_t = pref[h + 1] - pref[i + 1]
                        total_merges = used + merges_needed
                        # Update dp[h][total_merges][new_eff_t]
                        prev = dp[h][total_merges].get(new_eff_t)
                        if prev is None or new_cost < prev:
                            dp[h][total_merges][new_eff_t] = new_cost

        # The answer is the minimum cost at the last sign index with exactly k merges
        last_states = dp[n - 1][k]
        if not last_states:
            # No valid sequence of exactly k merges (shouldn't happen under constraints)
            return -1
        return min(last_states.values())
