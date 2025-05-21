class Solution:
    def maximumANDSum(self, nums, numSlots):
        memo = {}
        n = len(nums)

        def dp(i, mask):
            if i == n:
                return 0
            if (i, mask) in memo:
                return memo[(i, mask)]

            res = 0
            for slot in range(numSlots):
                count = (mask // (3 ** slot)) % 3
                if count < 2:
                    new_mask = mask + (3 ** slot)
                    res = max(res, (nums[i] & (slot + 1)) + dp(i + 1, new_mask))

            memo[(i, mask)] = res
            return res

        return dp(0, 0)
