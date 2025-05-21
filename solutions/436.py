import bisect

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        res = []
        
        for start, end in intervals:
            idx = bisect.bisect_left(starts, (end,))
            if idx < n:
                res.append(starts[idx][1])
            else:
                res.append(-1)
        
        return res
