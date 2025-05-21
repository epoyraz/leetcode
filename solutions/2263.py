class Solution:
    def maxRunTime(self, n, batteries):
        total = sum(batteries)
        left, right = 0, total // n

        def can_run_all(t):
            return sum(min(b, t) for b in batteries) >= t * n

        while left < right:
            mid = (left + right + 1) // 2
            if can_run_all(mid):
                left = mid
            else:
                right = mid - 1

        return left
