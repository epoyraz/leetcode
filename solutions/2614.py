class Solution:
    def maximumCount(self, nums):
        import bisect
        # First positive number index
        pos_index = bisect.bisect_right(nums, 0)
        # First zero index is where negatives end
        neg_index = bisect.bisect_left(nums, 0)
        pos = len(nums) - pos_index
        neg = neg_index
        return max(pos, neg)
