class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(n):
            original = n
            while n > 0:
                d = n % 10
                if d == 0 or original % d != 0:
                    return False
                n //= 10
            return True
        
        res = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                res.append(num)
        return res
