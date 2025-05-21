class Solution:
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        # 1) Compute L[i]: LIS ending at i
        L = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if L[j] + 1 > L[i]:
                        L[i] = L[j] + 1
        
        # 2) Compute R[i]: LIS (from right) starting at i = LDS from i
        R = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]:
                    if R[j] + 1 > R[i]:
                        R[i] = R[j] + 1
        
        # 3) Find best mountain
        best = 0
        for i in range(1, n-1):
            if L[i] > 1 and R[i] > 1:  # valid peak
                length = L[i] + R[i] - 1
                if length > best:
                    best = length
        
        # 4) Answer = remove the rest
        return n - best
