class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_strictly_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True

        n = len(nums)
        count = 0
        
        # Try every possible subarray [i..j]
        for i in range(n):
            for j in range(i, n):
                new_arr = nums[:i] + nums[j+1:]
                if is_strictly_increasing(new_arr):
                    count += 1
        
        return count
