import bisect

class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            right = heaters[idx] - house if idx < len(heaters) else float('inf')
            left = house - heaters[idx - 1] if idx > 0 else float('inf')
            res = max(res, min(left, right))
        return res
