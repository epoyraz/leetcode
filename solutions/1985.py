class Solution:
    def maxSumMinProduct(self, nums):
        mod = 10**9 + 7
        n = len(nums)
        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        # previous smaller element index
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        # next smaller element index
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        # compute max min-product
        ans = 0
        for i in range(n):
            total = prefix[right[i]] - prefix[left[i] + 1]
            ans = max(ans, nums[i] * total)
        return ans % mod
