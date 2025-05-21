class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            # Pop all shorter people; each pop is one visible person
            while stack and h > stack[-1]:
                ans[i] += 1
                stack.pop()
            # If there's still someone taller or equal, you see that one too
            if stack:
                ans[i] += 1
            # Add yourself to the stack
            stack.append(h)
        return ans
