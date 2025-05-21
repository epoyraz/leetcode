class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small.pop(0)
            else:
                nums[i] = large.pop(0)
