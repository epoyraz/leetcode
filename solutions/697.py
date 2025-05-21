class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        
        degree = max(count.values())
        res = len(nums)
        for x in count:
            if count[x] == degree:
                res = min(res, right[x] - left[x] + 1)
        return res
