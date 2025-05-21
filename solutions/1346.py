class Solution(object):
    def maximumTop(self, nums, k):
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            return nums[0] if k % 2 == 0 else -1
        if k == 1:
            return nums[1]
        if k > n:
            return max(nums)
        best = max(nums[:k - 1])               # take the largest among the first k-1 removed
        if k < n:                              # or leave the k-th element on top
            best = max(best, nums[k])
        return best
