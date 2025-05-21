class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the longest sequential prefix
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Use a set for fast lookup
        s = set(nums)

        # Return the smallest x >= total that is not in the array
        while total in s:
            total += 1
        return total
