class Solution(object):
    def addRungs(self, rungs, dist):
        prev = 0
        added = 0
        for h in rungs:
            gap = h - prev
            if gap > dist:
                added += (gap + dist - 1) // dist - 1
            prev = h
        return added
