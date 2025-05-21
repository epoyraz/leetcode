class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        n = len(nums)
        for i, v in enumerate(nums):
            good = True
            # compare to left neighbour k steps away, if it exists
            if i - k >= 0 and v <= nums[i - k]:
                good = False
            # compare to right neighbour k steps away, if it exists
            if i + k < n and v <= nums[i + k]:
                good = False
            if good:
                total += v
        return total
