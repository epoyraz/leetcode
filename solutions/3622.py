class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        if not nums:
            return 0
        n = len(nums)
        mn = min(nums)
        mx = max(nums)
        low = mn - k
        high = mx + k
        size = high - low + 1
        offset = -low
        freq = [0] * size
        for v in nums:
            freq[v + offset] += 1
        ps = [0] * (size + 1)
        for i in range(size):
            ps[i+1] = ps[i] + freq[i]
        res = 0
        for i in range(size):
            base = freq[i]
            L = i - k
            if L < 0:
                L = 0
            R = i + k
            if R >= size:
                R = size - 1
            total = ps[R+1] - ps[L]
            cand = total - base
            cur = base + (cand if cand < numOperations else numOperations)
            if cur > res:
                res = cur
        return res
