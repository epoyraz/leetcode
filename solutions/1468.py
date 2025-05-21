class Solution:
    def checkIfExist(self, arr):
        s = set(arr)
        # Special case: zero doubled is zero, need at least two zeros
        if arr.count(0) > 1:
            return True
        # For any non-zero x, check if 2*x exists
        for x in arr:
            if x != 0 and 2 * x in s:
                return True
        return False
