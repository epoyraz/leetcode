class Solution:
    def findSolution(self, customfunction, z):
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif val < z:
                x += 1
            else:
                y -= 1
        return res
