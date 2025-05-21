class Solution:
    def arrayChange(self, nums, operations):
        # Map each value to its index in nums
        pos = {val: i for i, val in enumerate(nums)}
        
        # Apply each operation
        for old, new in operations:
            idx = pos.pop(old)   # get and remove the old value's index
            nums[idx] = new      # replace in the array
            pos[new] = idx       # record the new value's index
        
        return nums
