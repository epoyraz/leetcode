import bisect

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # Build prefix sum: pre[k] = sum of nums[0..k-1]
        pre = [0] * (n+1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        total = pre[n]
        
        ans = 0
        # i is the length of the 'left' segment: valid i in [1 .. n-2]
        for i in range(1, n-1):
            left_sum = pre[i]
            # lower bound on pre[j] is 2*left_sum
            lo = bisect.bisect_left(pre, 2*left_sum, i+1, n)
            # upper bound on pre[j] is floor((total+left_sum)/2)
            bound = (total + left_sum) // 2
            hi = bisect.bisect_right(pre, bound, i+1, n) - 1
            
            if lo <= hi:
                ans = (ans + (hi - lo + 1)) % MOD
        
        return ans
