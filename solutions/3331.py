class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        operations = 0
        for num in nums:
            if num >= k:
                break
            operations += 1
        return operations
