class Solution:
    def zeroFilledSubarray(self, nums):
        total = 0
        streak = 0
        
        for x in nums:
            if x == 0:
                streak += 1
            else:
                # add all subarrays within the completed zero-streak
                total += streak * (streak + 1) // 2
                streak = 0
        
        # account for a trailing zero-streak
        total += streak * (streak + 1) // 2
        
        return total
