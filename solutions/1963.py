class Solution(object):
    def getXORSum(self, arr1, arr2):
        x = 0
        for v in arr1:
            x ^= v
        y = 0
        for v in arr2:
            y ^= v
        return x & y
