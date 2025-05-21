from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            count = Counter(window)
            
            # Sort by (-frequency, -value) to prioritize:
            # - higher frequency first
            # - for ties, higher value first
            top = sorted(count.items(), key=lambda t: (-t[1], -t[0]))[:x]
            
            # Include all occurrences of top x elements
            total = 0
            top_set = set(val for val, _ in top)
            for num in window:
                if num in top_set:
                    total += num
            
            res.append(total)
        
        return res
