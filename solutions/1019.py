class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        i = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
            i -= 1

        return result
