class Solution:
    def maximumTastiness(self, price, k):
        price.sort()
        
        def can(diff):
            # Greedily pick candies with at least `diff` apart
            count = 1
            last = price[0]
            for p in price[1:]:
                if p - last >= diff:
                    count += 1
                    last = p
                    if count == k:
                        return True
            return False
        
        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
