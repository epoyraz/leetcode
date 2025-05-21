class Solution:
    def checkZeroOnes(self, s):
        max1 = max0 = curr1 = curr0 = 0
        for ch in s:
            if ch == '1':
                curr1 += 1
                curr0 = 0
            else:
                curr0 += 1
                curr1 = 0
            max1 = max(max1, curr1)
            max0 = max(max0, curr0)
        return max1 > max0
