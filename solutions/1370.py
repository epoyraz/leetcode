class Solution:
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict

        count = defaultdict(int)
        count[0] = 1
        res = odd = 0

        for num in nums:
            if num % 2 == 1:
                odd += 1
            res += count[odd - k]
            count[odd] += 1

        return res
