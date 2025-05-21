from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. Count frequencies
        freq = Counter(nums)
        
        # 2. Determine the maximum frequency
        max_freq = max(freq.values())
        
        # 3. Sum the frequencies of all elements having that maximum frequency
        total = sum(count for count in freq.values() if count == max_freq)
        
        return total
