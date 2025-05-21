class Solution(object):
    def maximumSumOfHeights(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)

        # Compute left sums (non-increasing when going backward from peak)
        left = [0] * n
        stack = []
        total = 0
        for i in range(n):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                stack.pop()
            if not stack:
                left[i] = h * (i + 1)
            else:
                j = stack[-1]
                left[i] = left[j] + h * (i - j)
            stack.append(i)

        # Compute right sums (non-increasing when going forward from peak)
        right = [0] * n
        stack = []
        for i in reversed(range(n)):
            h = heights[i]
            while stack and heights[stack[-1]] > h:
                stack.pop()
            if not stack:
                right[i] = h * (n - i)
            else:
                j = stack[-1]
                right[i] = right[j] + h * (j - i)
            stack.append(i)

        # Try every peak and take max total
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left[i] + right[i] - heights[i])

        return max_total
