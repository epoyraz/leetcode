class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        def canPlaceBalls(min_dist):
            count = 1
            last = position[0]
            for i in range(1, len(position)):
                if position[i] - last >= min_dist:
                    count += 1
                    last = position[i]
                    if count == m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
