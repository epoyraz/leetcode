class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        insert_pos = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos
