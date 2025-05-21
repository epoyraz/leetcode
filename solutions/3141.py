class Solution(object):
    def minSizeSubarray(self, nums, target):
        n = len(nums)
        S = sum(nums)
        k, rem = divmod(target, S)
        if rem == 0:
            return k * n
        # Two-pointer on nums concatenated twice, window length <= n
        arr = nums + nums
        L_rem = float('inf')
        curr = 0
        l = 0
        for r, v in enumerate(arr):
            curr += v
            # shrink while sum too big or window too long
            while l <= r and (curr > rem or r - l + 1 > n):
                curr -= arr[l]
                l += 1
            if curr == rem:
                L_rem = min(L_rem, r - l + 1)
        if L_rem == float('inf'):
            return -1
        return k * n + L_rem
