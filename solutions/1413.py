class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        
        # Step 1: Compute prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (prefix[i][j + 1] + prefix[i + 1][j] 
                                        - prefix[i][j] + mat[i][j])
        
        # Helper to check if any k x k square has sum <= threshold
        def valid(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (prefix[i + k][j + k] - prefix[i][j + k] 
                             - prefix[i + k][j] + prefix[i][j])
                    if total <= threshold:
                        return True
            return False

        # Step 2: Binary search on side length
        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if valid(mid):
                left = mid
            else:
                right = mid - 1

        return left
