class Solution(object):
    def minIncrementOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # cover[i] = True if nums[i] >= k initially
        cover = [num >= k for num in nums]
        # cost to raise nums[i] up to k (0 if already >= k)
        cost = [max(0, k - num) for num in nums]

        def solve_segment(costs):
            """
            Given a list of costs for a consecutive segment of zeros (where cover=False),
            return the minimum total cost to select some positions so that
            no three consecutive positions remain unselected.
            Uses a small DP over states of consecutive unselected count.
            """
            L = len(costs)
            INF = 10**30
            # dp[d] = min cost up to previous position,
            # with exactly d consecutive unselected positions at the end (d in {0,1,2})
            dp = [0, INF, INF]

            for w in costs:
                ndp = [INF, INF, INF]
                for d in (0, 1, 2):
                    cur = dp[d]
                    if cur >= INF:
                        continue
                    # Option 1: select this position (pay w), resets run of unselected
                    ndp[0] = min(ndp[0], cur + w)
                    # Option 2: do not select: only if it won't create 3 unselected in a row
                    if d < 2:
                        ndp[d + 1] = min(ndp[d + 1], cur)
                dp = ndp

            # any ending run of length 0,1,2 is fine
            res = min(dp)
            return res if res < INF else None

        ans = 0
        i = 0
        while i < n:
            if cover[i]:
                i += 1
            else:
                # find the end of this zero-segment
                j = i
                while j < n and not cover[j]:
                    j += 1
                seg_cost = solve_segment(cost[i:j])
                if seg_cost is None:
                    return -1
                ans += seg_cost
                i = j

        return ans
