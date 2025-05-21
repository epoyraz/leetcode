class Solution:
    def checkArray(self, nums, k):
        n = len(nums)
        delta = [0] * (n + 1)
        cur = 0

        for i in range(n):
            cur += delta[i]
            diff = nums[i] - cur

            if diff < 0:
                return False
            if diff > 0:
                if i + k > n:
                    return False
                cur += diff
                delta[i + k] -= diff

        return True
