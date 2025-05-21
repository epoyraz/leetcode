class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        while len(nums) > 0:
            seen = set()
            duplicate = False
            for num in nums:
                if num in seen:
                    duplicate = True
                    break
                seen.add(num)
            if not duplicate:
                break
            ops += 1
            nums = nums[3:]
        return ops
