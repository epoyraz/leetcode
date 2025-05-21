class Solution(object):
    def sumOfNumberAndReverse(self, num):
        def reverse(x):
            r = 0
            while x:
                r = r*10 + x%10
                x //= 10
            return r
        
        for x in range(num+1):
            if x + reverse(x) == num:
                return True
        return False
