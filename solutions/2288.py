class Solution(object):
    def countOperations(self, num1, num2):
        ops = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                ops += num1 // num2
                num1 %= num2
            else:
                ops += num2 // num1
                num2 %= num1
        return ops
