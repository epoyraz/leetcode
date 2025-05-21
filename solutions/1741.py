class Solution:
    def frequencySort(self, nums):
        from collections import Counter
        freq = Counter(nums)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
