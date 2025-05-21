class Solution:
    def subtractProductAndSum(self, n):
        product = 1
        summation = 0
        while n > 0:
            digit = n % 10
            product *= digit
            summation += digit
            n //= 10
        return product - summation
