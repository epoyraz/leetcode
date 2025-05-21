class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_non_decreasing(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
        
        ops = 0
        # If already non-decreasing, no operations needed
        if is_non_decreasing(nums):
            return 0
        
        while len(nums) > 1:
            # Find the leftmost adjacent pair with minimum sum
            min_sum = nums[0] + nums[1]
            idx = 0
            for i in range(1, len(nums)-1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            # Replace that pair with their sum
            nums = nums[:idx] + [min_sum] + nums[idx+2:]
            ops += 1
            # Check if we've achieved non-decreasing order
            if is_non_decreasing(nums):
                return ops
        
        # If we collapse down to a single element, it's trivially non-decreasing
        return ops
