class Solution:
    def partitionArray(self, nums, k):
        # Sort the numbers to group by value
        nums.sort()
        count = 1
        start = nums[0]
        
        for x in nums:
            # If the current number is too far from the group's minimum,
            # start a new subsequence
            if x - start > k:
                count += 1
                start = x
        
        return count
