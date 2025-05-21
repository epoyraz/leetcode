class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDivide(maxSize):
            operations = 0
            for num in nums:
                operations += (num - 1) // maxSize
            return operations <= maxOperations

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid
            else:
                left = mid + 1
        return left
