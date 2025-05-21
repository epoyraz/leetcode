class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        # compute sum of digits
        s = 0
        t = x
        while t:
            s += t % 10
            t //= 10
        
        # check Harshad condition
        return s if x % s == 0 else -1
