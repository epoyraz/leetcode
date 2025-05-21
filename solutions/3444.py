from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # 1) Build frequency array for nums1 up to its maximum value
        M = max(nums1)
        freqA = [0] * (M + 1)
        for a in nums1:
            freqA[a] += 1
        
        # 2) Build a Counter of all d = b * k that might actually divide something in nums1
        freqD = Counter()
        for b in nums2:
            d = b * k
            if d <= M:
                freqD[d] += 1
        
        # 3) For each distinct d, add up freqD[d] * (count of multiples of d in nums1)
        ans = 0
        for d, cntD in freqD.items():
            # walk through d, 2d, 3d, ... â¤ M
            for multiple in range(d, M + 1, d):
                ans += cntD * freqA[multiple]
        
        return ans
