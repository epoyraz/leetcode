class Solution:
    def findKthNumber(self, n, k):
        def get_steps(n, curr, next_curr):
            steps = 0
            while curr <= n:
                steps += min(n + 1, next_curr) - curr
                curr *= 10
                next_curr *= 10
            return steps
        
        curr = 1
        k -= 1  # because we start from 1 already
        
        while k > 0:
            steps = get_steps(n, curr, curr + 1)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10
        
        return curr
