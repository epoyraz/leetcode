class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
