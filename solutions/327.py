class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            j = k = mid
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count
        
        return sort(0, len(prefix))
