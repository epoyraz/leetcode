class Solution(object):
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)
        dp = [set() for _ in range(n+1)]
        dp[0].add(0)
        
        for num in nums:
            for i in range(n-1, -1, -1):
                for s in dp[i]:
                    dp[i+1].add(s + num)
        
        for k in range(1, n):
            if total * k % n == 0 and (total * k // n) in dp[k]:
                return True
        return False
