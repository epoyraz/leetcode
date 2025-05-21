import sys
sys.setrecursionlimit(10000)

class Solution(object):
    def minCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        # dp[i][j]: min cost to clear array [nums[j]] + nums[i:]
        # i: start index of suffix; j: index of survivor at front
        dp = [[-1] * n for _ in range(n + 1)]
        
        def solve(i, j):
            # dp on state (i, j)
            if dp[i][j] != -1:
                return dp[i][j]
            # Remaining array length
            rem = 1 + (n - i)
            # Base: if rem <= 2, single final operation
            if rem == 2:
                dp[i][j] = max(nums[j], nums[i])
                return dp[i][j]
            if rem == 1:
                dp[i][j] = nums[j]
                return dp[i][j]
            
            # General: at least 3 elements in [nums[j]] + nums[i:]
            a0 = nums[j]
            a1 = nums[i]
            a2 = nums[i + 1]
            # Next suffix starts at k = i+2
            k = i + 2
            
            # Option 1: remove a0 and a1, survivor becomes a2 at index i+1
            cost1 = max(a0, a1) + solve(k, i + 1)
            # Option 2: remove a0 and a2, survivor becomes a1 at index i
            cost2 = max(a0, a2) + solve(k, i)
            # Option 3: remove a1 and a2, survivor remains a0 at index j
            cost3 = max(a1, a2) + solve(k, j)
            
            dp[i][j] = min(cost1, cost2, cost3)
            return dp[i][j]
        
        # Initial removal among first three of nums[0], nums[1], nums[2]
        a0, a1, a2 = nums[0], nums[1], nums[2]
        # Suffix start index
        k = 3
        ans1 = max(a0, a1) + solve(k, 2)  # remove indices 0 & 1
        ans2 = max(a0, a2) + solve(k, 1)  # remove 0 & 2
        ans3 = max(a1, a2) + solve(k, 0)  # remove 1 & 2
        
        return min(ans1, ans2, ans3)