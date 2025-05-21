class Solution:
    def intersection(self, nums):
        counts = {}
        n = len(nums)
        for arr in nums:
            for x in arr:
                counts[x] = counts.get(x, 0) + 1
        
        # Collect those present in all n arrays
        res = [x for x, c in counts.items() if c == n]
        res.sort()
        return res
