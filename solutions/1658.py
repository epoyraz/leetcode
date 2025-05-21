class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        rightmost_one = []

        for row in grid:
            pos = -1
            for j in reversed(range(n)):
                if row[j] == 1:
                    pos = j
                    break
            rightmost_one.append(pos)

        swaps = 0
        for i in range(n):
            j = i
            while j < n and rightmost_one[j] > i:
                j += 1
            if j == n:
                return -1
            # Bubble the row up
            while j > i:
                rightmost_one[j], rightmost_one[j - 1] = rightmost_one[j - 1], rightmost_one[j]
                swaps += 1
                j -= 1

        return swaps
