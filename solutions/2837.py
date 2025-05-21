class Solution:
    def makeTheIntegerZero(self, num1, num2):
        for k in range(1, 61):  # Try using k operations
            target = num1 - k * num2
            if target < k:
                continue
            if bin(target).count('1') <= k:
                return k
        return -1
