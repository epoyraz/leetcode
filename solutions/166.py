class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        
        res = []
        
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return ''.join(res)
        
        res.append('.')
        map_remainder = {}
        
        while remainder != 0:
            if remainder in map_remainder:
                res.insert(map_remainder[remainder], '(')
                res.append(')')
                break
            map_remainder[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(res)
