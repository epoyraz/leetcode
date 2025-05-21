class Solution:
    def numberOfPairs(self, nums):
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        
        pairs = 0
        for cnt in counts.values():
            pairs += cnt // 2
        
        leftover = len(nums) - 2 * pairs
        return [pairs, leftover]
