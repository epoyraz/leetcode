class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7

        # prev[i] = index of previous smaller element before i (or -1)
        prev = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # next_[i] = index of next smaller-or-equal element after i (or n)
        next_ = [0] * n
        stack = []  # reset the stack instead of using clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_[i] = stack[-1] if stack else n
            stack.append(i)

        # sum contributions of each element as the minimum
        ans = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            ans = (ans + arr[i] * left * right) % mod

        return ans
