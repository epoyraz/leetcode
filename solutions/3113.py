class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        n = len(maxHeights)
        left = [0] * n
        right = [0] * n

        # Process left sums
        stack = []
        for i in range(n):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            if not stack:
                left[i] = maxHeights[i] * (i + 1)
            else:
                j = stack[-1]
                left[i] = left[j] + maxHeights[i] * (i - j)
            stack.append(i)

        # Process right sums
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            if not stack:
                right[i] = maxHeights[i] * (n - i)
            else:
                j = stack[-1]
                right[i] = right[j] + maxHeights[i] * (j - i)
            stack.append(i)

        # Combine left and right sums at each peak (subtract maxHeights[i] once)
        max_total = 0
        for i in range(n):
            max_total = max(max_total, left[i] + right[i] - maxHeights[i])

        return max_total
