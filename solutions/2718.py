import bisect

class Solution:
    def minOperations(self, nums, queries):
        # Sort nums and build prefix sums
        nums.sort()
        n = len(nums)
        prefix = [0] * (n+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i] + x
        
        ans = []
        for q in queries:
            # count of nums < q
            idx = bisect.bisect_left(nums, q)
            # cost to raise all nums[:idx] up to q
            left_cost  = q*idx - prefix[idx]
            # cost to lower all nums[idx:] down to q
            right_cost = (prefix[n] - prefix[idx]) - q*(n-idx)
            ans.append(left_cost + right_cost)
        return ans
