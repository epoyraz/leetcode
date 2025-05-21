class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        return [findLeft(nums, target), findRight(nums, target)]
