class Solution(object):
    def getLucky(self, s, k):
        # Compute initial digit-sum of the concatenated positions
        total = 0
        for ch in s:
            v = ord(ch) - ord('a') + 1
            # add sum of digits of v
            if v < 10:
                total += v
            else:
                total += v // 10 + v % 10
        
        # Perform k-1 further digit-sum transforms
        for _ in range(k-1):
            t = 0
            while total > 0:
                t += total % 10
                total //= 10
            total = t
        
        return total
