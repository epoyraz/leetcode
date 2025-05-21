class Solution(object):
    def findKthNumber(self, m, n, k):
        def count(x):
            total = 0
            for i in range(1, m + 1):
                total += min(x // i, n)
            return total
        
        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
