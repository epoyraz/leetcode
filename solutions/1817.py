class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Number of complete weeks and leftover days
        w, r = divmod(n, 7)
        
        # Sum from full weeks:
        # Each week i (0-based) contributes 28 + 7*i
        # Sum_{i=0 to w-1} (28 + 7*i) = 28*w + 7 * (w*(w-1)//2)
        full_weeks_sum = 28 * w + 7 * (w * (w - 1) // 2)
        
        # Sum from leftover r days in week w:
        # Day k in that week gives (k + w) for k=1..r
        # Sum = sum(k, k=1..r) + w * r = r*(r+1)//2 + w*r
        leftover_sum = r * (r + 1) // 2 + w * r
        
        return full_weeks_sum + leftover_sum
