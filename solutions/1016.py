from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums, k):
        count = defaultdict(int)
        count[0] = 1  # prefix sum % k == 0 initially
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            mod = prefix % k
            if mod < 0:
                mod += k  # ensure mod is non-negative

            result += count[mod]
            count[mod] += 1

        return result
