from collections import Counter

class Solution(object):
    def countSubarrays(self, nums, k):
        pos = nums.index(k)
        count = Counter()
        s = 0
        count[0] = 1
        # count prefix sums on the left of k
        for i in range(pos - 1, -1, -1):
            s += 1 if nums[i] > k else -1
            count[s] += 1
        # scan to the right including k
        ans = 0
        r = 0
        for j in range(pos, len(nums)):
            if nums[j] > k:
                r += 1
            elif nums[j] < k:
                r -= 1
            ans += count[-r] + count[1 - r]
        return ans
