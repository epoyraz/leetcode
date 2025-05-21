class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        # extract and sort x-coordinates
        xs = sorted(x for x, _ in points)
        n = len(xs)
        ans = 0
        i = 0
        
        while i < n:
            # place one rectangle covering [xs[i], xs[i] + w]
            start = xs[i]
            limit = start + w
            ans += 1
            # skip all points covered by this interval
            while i < n and xs[i] <= limit:
                i += 1
        
        return ans
