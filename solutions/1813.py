class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0
        
        for right, v in enumerate(nums):
            while v in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(v)
            curr_sum += v
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum
