class Solution:
    def fillCups(self, amount):
        total = amount[0] + amount[1] + amount[2]
        mx = max(amount)
        # You can fill at most 2 cups per second, but they must be different types.
        # So you need at least ceil(total/2) seconds, and also at least as many seconds
        # as the largest single type (since you can't pair beyond the sum of the other two).
        return max(mx, (total + 1) // 2)
