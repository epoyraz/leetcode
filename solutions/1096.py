class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        n = len(nums)
        # prefix sums
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        # sums of windows
        A = [0] * n  # firstLen-window ending at i
        B = [0] * n  # secondLen-window ending at i
        for i in range(firstLen - 1, n):
            A[i] = pre[i+1] - pre[i+1-firstLen]
        for i in range(secondLen - 1, n):
            B[i] = pre[i+1] - pre[i+1-secondLen]
        # best prefix maxima
        bestA = [0] * n
        bestB = [0] * n
        best = 0
        for i in range(n):
            best = max(best, A[i])
            bestA[i] = best
        best = 0
        for i in range(n):
            best = max(best, B[i])
            bestB[i] = best
        # combine: A before B or B before A
        ans = 0
        # A before B
        for i in range(secondLen, n):
            ans = max(ans, bestA[i-secondLen] + B[i])
        # B before A
        for i in range(firstLen, n):
            ans = max(ans, bestB[i-firstLen] + A[i])
        return ans
