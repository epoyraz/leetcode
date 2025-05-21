class Solution(object):
    def minEatingSpeed(self, piles, h):
        def can_eat_all(speed):
            return sum((pile + speed - 1) // speed for pile in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1
        return left
