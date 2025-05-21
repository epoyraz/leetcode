class Solution:
    def xorAllNums(self, nums1, nums2):
        xor1 = 0
        for x in nums1:
            xor1 ^= x
        xor2 = 0
        for x in nums2:
            xor2 ^= x

        res = 0
        # If len(nums2) is odd, xor1 contributes
        if len(nums2) & 1:
            res ^= xor1
        # If len(nums1) is odd, xor2 contributes
        if len(nums1) & 1:
            res ^= xor2
        return res
