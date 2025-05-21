class Solution:
    def minimumNumbers(self, num, k):
        # Empty set yields sum 0
        if num == 0:
            return 0
        
        # Special case k=0: must use multiples of 10, so num%10==0
        if k == 0:
            return 1 if num % 10 == 0 else -1
        
        # For k>0, search m from 1..num//k
        max_m = num // k
        for m in range(1, max_m + 1):
            if (num - m * k) % 10 == 0:
                return m
        
        return -1
