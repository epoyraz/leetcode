class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if m * k > n:
            return -1  # Not enough flowers

        def canMake(day):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        low, high = min(bloomDay), max(bloomDay)
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
