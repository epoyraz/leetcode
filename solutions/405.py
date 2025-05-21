class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        res = ""
        
        num &= 0xFFFFFFFF  # Handle negative numbers with two's complement
        
        while num > 0:
            res = hex_chars[num % 16] + res
            num //= 16
        
        return res
