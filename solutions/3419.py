class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        """
        :type points: List[List[int]]
        :type s: str
        :rtype: int
        """
        def is_valid(mid):
            seen = set()
            for i in range(len(points)):
                x, y = points[i]
                if max(abs(x), abs(y)) <= mid:
                    if s[i] in seen:
                        return False
                    seen.add(s[i])
            return True

        low, high = 0, max(max(abs(x), abs(y)) for x, y in points)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if is_valid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        # Now count the number of points inside the square of size `ans`
        seen = set()
        count = 0
        for i in range(len(points)):
            x, y = points[i]
            if max(abs(x), abs(y)) <= ans and s[i] not in seen:
                seen.add(s[i])
                count += 1

        return count
