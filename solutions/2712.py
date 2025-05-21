class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        j = n // 2
        count = 0

        while i < n // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                count += 2
                i += 1
            j += 1

        return count
