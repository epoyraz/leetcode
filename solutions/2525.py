class Solution(object):
    def countDistinctIntegers(self, nums):
        seen = set(nums)
        def rev(x):
            r = 0
            while x:
                r = r*10 + x%10
                x //= 10
            return r
        for x in nums:
            seen.add(rev(x))
        return len(seen)
