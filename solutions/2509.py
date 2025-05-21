class Solution:
    def minimizeXor(self, num1, num2):
        # Count how many 1-bits we need in x
        k = bin(num2).count('1')
        
        # Record positions of 1-bits and 0-bits in num1
        ones = []
        zeros = []
        for i in range(31, -1, -1):
            if (num1 >> i) & 1:
                ones.append(i)
            else:
                zeros.append(i)
        
        x = 0
        # Use as many 1-bits from num1's 1-positions (highest first)
        c1 = min(k, len(ones))
        for i in ones[:c1]:
            x |= 1 << i
        
        # Remaining ones go into zeros at the lowest positions
        rem = k - c1
        for i in sorted(zeros)[:rem]:
            x |= 1 << i
        
        return x
