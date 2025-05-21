class Solution(object):
    def maxChunksToSorted(self, arr):
        res = 0
        curr_max = 0
        for i, num in enumerate(arr):
            curr_max = max(curr_max, num)
            if curr_max == i:
                res += 1
        return res
