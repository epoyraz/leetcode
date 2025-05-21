class Solution(object):
    def preimageSizeFZF(self, k):
        def zeta(x):
            res = 0
            while x:
                x //= 5
                res += x
            return res
        
        def search(k):
            low, high = 0, 5 * (k + 1)
            while low < high:
                mid = (low + high) // 2
                if zeta(mid) < k:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        return 5 if zeta(search(k)) == k else 0
