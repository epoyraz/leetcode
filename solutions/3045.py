class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Sorted target
        target = sorted(nums)
        # Find index of the minimal element (target[0]) in nums
        first = target[0]
        idx = nums.index(first)
        # Compute required right-shifts k so that idx -> 0
        k = (n - idx) % n
        # Apply the rotation and check
        # rotate_right by k: take last k elements, then the rest
        if k == 0:
            rotated = nums
        else:
            rotated = nums[-k:] + nums[:-k]
        return k if rotated == target else -1
