class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # If k is large enough, we can take the whole array.
        if k >= n - 1:
            return n

        # 1) Compress values to 0..d-1
        uniq = {}
        comp = []
        for x in nums:
            if x not in uniq:
                uniq[x] = len(uniq)
            comp.append(uniq[x])
        d = len(uniq)

        # 2) dp[t][v] = best subseq length ending with value v using <= t transitions
        # Initialize all 0.
        dp = [[0] * d for _ in range(k + 1)]

        # For each t, track the best and second-best dp[t][*] and which value achieves them.
        best1_dp = [0] * (k + 1)
        best1_val = [-1] * (k + 1)
        best2_dp = [0] * (k + 1)
        best2_val = [-1] * (k + 1)

        # 3) Sweep through the array
        for v in comp:
            # process transitions in descending order
            for t in range(k, -1, -1):
                old = dp[t][v]
                # (a) extend same-value chain (no new transition)
                cand = old + 1

                # (b) or extend best different-value chain from dp[t-1] (one new transition)
                if t > 0:
                    # pick the top dp[t-1] unless it came from v, in which case pick the runner-up
                    if best1_val[t-1] != v:
                        other_best = best1_dp[t-1]
                    else:
                        other_best = best2_dp[t-1]
                    cand = max(cand, other_best + 1)

                # update dp[t][v]
                dp[t][v] = cand

                # 4) update the best1/2 trackers for level t
                if best1_val[t] == v:
                    # we just improved the existing champion
                    best1_dp[t] = cand
                else:
                    if cand > best1_dp[t]:
                        # new champ pushes the old champ to runner-up
                        best2_dp[t] = best1_dp[t]
                        best2_val[t] = best1_val[t]
                        best1_dp[t] = cand
                        best1_val[t] = v
                    elif cand > best2_dp[t]:
                        # new runner-up
                        best2_dp[t] = cand
                        best2_val[t] = v

        # The best you can do with <= k transitions is the top dp[k][*].
        return best1_dp[k]
