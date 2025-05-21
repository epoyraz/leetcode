class Solution(object):
    def maximumCandies(self, candies, k):
        lo, hi = 1, max(candies)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            cnt = 0
            for c in candies:
                cnt += c // mid
                if cnt >= k:
                    break
            if cnt >= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
