class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if a + c == b / 2.0:
                count += 1
        return count
