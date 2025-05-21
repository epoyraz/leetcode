class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = {}           # dp[v] = max runâlength ending at v
        ans = 0
        for x in nums:
            # lengths of the best run if we place this element at x or at x+1:
            without_bump = dp.get(x-1, 0) + 1
            with_bump    = dp.get(x,   0) + 1

            # update dp[x]  (no bump)
            if without_bump > dp.get(x, 0):
                dp[x] = without_bump
            # update dp[x+1]  (bump by 1)
            if with_bump > dp.get(x+1, 0):
                dp[x+1] = with_bump

            # track global best
            ans = max(ans, dp[x], dp[x+1])

        return ans
