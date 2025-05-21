class Solution:
    def totalStrength(self, strength):
        MOD = 10**9 + 7
        n = len(strength)
        
        # Compute previous less element (strictly less)
        L = [-1] * n
        stack = []
        for i, val in enumerate(strength):
            while stack and strength[stack[-1]] >= val:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Compute next less element (strictly less)
        R = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            val = strength[i]
            while stack and strength[stack[-1]] > val:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Prefix sums P and prefix-of-prefix PP
        P = [0] * (n+1)
        for i in range(n):
            P[i+1] = (P[i] + strength[i]) % MOD
        PP = [0] * (n+2)
        for i in range(n+1):
            PP[i+1] = (PP[i] + P[i]) % MOD
        
        ans = 0
        for i in range(n):
            left_count  = i - L[i]       # number of choices for start
            right_count = R[i] - i       # number of choices for end
            
            # Sum over ends: sum_{r=i..R[i]-1} P[r+1] = PP[R[i]+1] - PP[i+1]
            sumR = (PP[R[i]+1] - PP[i+1]) % MOD
            # Sum over starts: sum_{l=L[i]+1..i} P[l] = PP[i+1] - PP[L[i]+1]
            sumL = (PP[i+1] - PP[L[i]+1]) % MOD
            
            total_subarray_sum = (left_count * sumR - right_count * sumL) % MOD
            ans = (ans + strength[i] * total_subarray_sum) % MOD
        
        return ans
