class Solution:
    def shipWithinDays(self, weights, days):
        def canShip(cap):
            curr, d = 0, 1
            for w in weights:
                if curr + w > cap:
                    d += 1
                    curr = 0
                curr += w
            return d <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left
