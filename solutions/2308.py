class Solution(object):
    def divideArray(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        for v in count.values():
            if v % 2 != 0:
                return False
        return True
