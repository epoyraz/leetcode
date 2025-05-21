class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        curr = 0
        freq = {0: 1}
        for x in nums:
            curr += x
            count += freq.get(curr - k, 0)
            freq[curr] = freq.get(curr, 0) + 1
        return count
