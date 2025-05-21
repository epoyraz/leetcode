class Solution:
    def kthLargestNumber(self, nums, k):
        nums.sort(key=lambda x: (len(x), x))
        return nums[-k]
