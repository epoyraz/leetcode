class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        # prefix_max[i] = max of nums[0..i]
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        # suffix_max[i] = max of nums[i..n-1]
        suffix_max = [0] * n
        suffix_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])
        res = 0
        # iterate j as middle index
        for j in range(1, n-1):
            max_i = prefix_max[j-1]
            max_k = suffix_max[j+1]
            diff = max_i - nums[j]
            if diff > 0 and max_k > 0:
                val = diff * max_k
                if val > res:
                    res = val
        return res