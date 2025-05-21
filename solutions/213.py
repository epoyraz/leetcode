class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(nums):
            prev = curr = 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))
