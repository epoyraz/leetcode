from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = nums[:]
        q = deque()
        q.append(0)
        max_sum = nums[0]
        
        for i in range(1, n):
            # Remove indices out of window
            if q and q[0] < i - k:
                q.popleft()

            dp[i] = max(dp[q[0]] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])

            # Maintain deque in decreasing dp order
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)

        return max_sum
