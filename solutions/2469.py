import bisect

class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        res = []
        for q in queries:
            k = bisect.bisect_right(prefix, q) - 1
            res.append(k)
        return res
