class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        P = n // 2
        
        # A[d] = count of pairs with original difference d
        A = [0] * (k+1)
        # freqR[r] = count of pairs whose "one-change range" R_i is exactly r
        freqR = [0] * (k+1)
        
        # Build A and freqR
        for i in range(P):
            a = nums[i]
            b = nums[n-1-i]
            d = abs(a - b)
            A[d] += 1
            
            # R = max(max(a,k-a), max(b,k-b))
            R = max(max(a, k-a), max(b, k-b))
            # R is in [0..k]
            freqR[R] += 1
        
        # Build B[X] = sum_{r >= X} freqR[r] via suffix sum
        B = [0] * (k+2)
        for X in range(k, -1, -1):
            B[X] = B[X+1] + freqR[X]
        
        # Find X that maximizes S[X] = A[X] + B[X]
        maxS = 0
        for X in range(k+1):
            s = A[X] + B[X]
            if s > maxS:
                maxS = s
        
        # Minimum total changes = 2*P - maxS
        return 2*P - maxS
