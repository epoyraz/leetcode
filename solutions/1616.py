class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4:
            return 0  # Can change all to the same number

        nums.sort()
        return min(
            nums[-1] - nums[3],   # remove 3 smallest
            nums[-2] - nums[2],   # remove 2 smallest + 1 largest
            nums[-3] - nums[1],   # remove 1 smallest + 2 largest
            nums[-4] - nums[0]    # remove 3 largest
        )
