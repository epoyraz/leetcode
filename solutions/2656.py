class Solution(object):
    def beautifulSubarrays(self, nums):
        from collections import Counter
        cnt = Counter()
        xor = 0
        cnt[0] = 1   # prefix before start
        for x in nums:
            xor ^= x
            cnt[xor] += 1

        res = 0
        for c in cnt.values():
            # choose any two equal prefixes
            res += c * (c - 1) // 2
        return res
