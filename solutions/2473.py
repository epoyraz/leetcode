class Solution:
    def maximumSum(self, nums):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        best = {}  # sum -> [max1, max2]
        ans = -1
        
        for x in nums:
            s = digit_sum(x)
            if s not in best:
                best[s] = [x, -1]
            else:
                a, b = best[s]
                if x > a:
                    b = a
                    a = x
                elif x > b:
                    b = x
                best[s] = [a, b]
            
            a, b = best[s]
            if b >= 0:
                ans = max(ans, a + b)
        
        return ans
