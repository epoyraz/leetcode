class Solution:
    def minOperations(self, nums):
        n = len(nums)
        # Get sorted list of unique values
        A = sorted(set(nums))
        
        max_keep = 0
        m = len(A)
        r = 0
        
        # Slide window over A: for each l, advance r so that A[r] - A[l] <= n-1
        for l in range(m):
            # Ensure r is at least l
            if r < l:
                r = l
            # Extend r while within a span of length n
            while r + 1 < m and A[r+1] - A[l] <= n - 1:
                r += 1
            # Window [l..r] fits within some consecutive block of size n
            max_keep = max(max_keep, r - l + 1)
        
        # We can keep at most max_keep original elements;
        # the rest must be changed.
        return n - max_keep
