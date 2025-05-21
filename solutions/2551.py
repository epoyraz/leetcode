class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        # 1) Apply the n-1 operations in order
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # 2) Shift all zeros to the end in-place
        write = 0
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        # Fill the remainder with zeros
        for i in range(write, n):
            nums[i] = 0
        
        return nums
