class Solution:
    def largestGoodInteger(self, num):
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                candidate = num[i] * 3
                if candidate > best:
                    best = candidate
        return best
