class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        total = 0
        curr_len = 1  # length of current maximal alternating segment
        
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                # still alternating, extend segment
                curr_len += 1
            else:
                # segment ends here
                total += curr_len * (curr_len + 1) // 2
                curr_len = 1
        
        # add the last segment
        total += curr_len * (curr_len + 1) // 2
        
        return total
