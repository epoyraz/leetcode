class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # dp[i][r]: best length ending at i with adjacentâsum mod == r
        dp = [[0]*k for _ in range(n)]
        ans = 1
        
        for i in range(n):
            dpi = dp[i]
            for j in range(i):
                r = (nums[j] + nums[i]) % k
                # either start new pair (length=2) or extend dp[j][r]
                val = dp[j][r] + 1 if dp[j][r] else 2
                if val > dpi[r]:
                    dpi[r] = val
                if val > ans:
                    ans = val
        
        return ans
