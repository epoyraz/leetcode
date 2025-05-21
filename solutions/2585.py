class Solution:
    def deleteGreatestValue(self, grid):
        for row in grid:
            row.sort()
        ans = 0
        for col in zip(*grid):
            ans += max(col)
        return ans
