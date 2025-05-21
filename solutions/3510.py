class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        maximumHeight.sort()
        n = len(maximumHeight)
        
        total = 0
        last_height = float('inf')  # Last height assigned

        for i in range(n - 1, -1, -1):
            height = min(maximumHeight[i], last_height - 1)
            if height <= 0:
                return -1
            total += height
            last_height = height

        return total
