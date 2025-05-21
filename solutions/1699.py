import collections

class Solution(object):
    def numTriplets(self, nums1, nums2):
        MOD = 10**9 + 7
        
        # frequency maps
        freq1 = collections.Counter(nums1)
        freq2 = collections.Counter(nums2)
        uniq1 = list(freq1.keys())
        uniq2 = list(freq2.keys())
        
        ans = 0
        
        # Type 1: nums1[i]^2 == nums2[j] * nums2[k]
        for x in uniq1:
            T = x * x
            # count pairs in nums2 whose product is T
            p = 0
            for v in uniq2:
                if T % v != 0:
                    continue
                w = T // v
                if w not in freq2:
                    continue
                if v < w:
                    p += freq2[v] * freq2[w]
                elif v == w:
                    c = freq2[v]
                    p += c * (c - 1) // 2
            ans = (ans + freq1[x] * p) % MOD
        
        # Type 2: nums2[i]^2 == nums1[j] * nums1[k]
        for y in uniq2:
            T = y * y
            # count pairs in nums1 whose product is T
            p = 0
            for v in uniq1:
                if T % v != 0:
                    continue
                w = T // v
                if w not in freq1:
                    continue
                if v < w:
                    p += freq1[v] * freq1[w]
                elif v == w:
                    c = freq1[v]
                    p += c * (c - 1) // 2
            ans = (ans + freq2[y] * p) % MOD
        
        return ans
