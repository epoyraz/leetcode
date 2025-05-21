from collections import Counter

class Solution:
    def countTriplets(self, nums):
        count = Counter()
        
        # Precompute all pairwise ANDs and their frequencies
        for a in nums:
            for b in nums:
                count[a & b] += 1

        result = 0
        for k in nums:
            for val, freq in count.items():
                if val & k == 0:
                    result += freq
        return result
