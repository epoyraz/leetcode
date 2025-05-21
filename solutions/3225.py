class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right, x in enumerate(nums):
            freq[x] += 1
            # If x exceeds k, shrink from left until freq[x] <= k
            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1
            # Now window [left..right] is good
            max_len = max(max_len, right - left + 1)
        
        return max_len
