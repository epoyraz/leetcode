class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # inc_len: length of current strictly increasing run ending at i
        # dec_len: length of current strictly decreasing run ending at i
        inc_len = dec_len = 1
        best = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_len += 1
            else:
                inc_len = 1
            
            if nums[i] < nums[i-1]:
                dec_len += 1
            else:
                dec_len = 1
            
            best = max(best, inc_len, dec_len)
        
        return best
