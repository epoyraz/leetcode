from collections import deque

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # dp[i] = max score to reach i
        dp = [0] * n
        dp[0] = nums[0]
        # deque will store indices of dp, in decreasing dp value
        dq = deque([0])
        
        for i in range(1, n):
            # remove indices outside the window [i-k, i-1]
            while dq and dq[0] < i - k:
                dq.popleft()
            # the best previous is at dq[0]
            dp[i] = nums[i] + dp[dq[0]]
            # maintain decreasing dp in deque
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        return dp[-1]
