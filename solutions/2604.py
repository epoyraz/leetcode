class Solution:
    def minOperations(self, nums1, nums2, k):
        # Special case: no change possible
        if k == 0:
            return 0 if nums1 == nums2 else -1
        
        n = len(nums1)
        diff_sum = 0
        pos_sum = 0
        
        for a, b in zip(nums1, nums2):
            d = b - a
            diff_sum += d
            # Each position must be reachable by Â±k steps
            if d % k != 0:
                return -1
            if d > 0:
                pos_sum += d
        
        # Total difference must cancel out
        if diff_sum != 0:
            return -1
        
        # Each operation moves exactly k units into one pos
        return pos_sum // k
