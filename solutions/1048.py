class Solution:
    def clumsy(self, n):
        stack = [n]
        n -= 1
        ops = 0
        while n > 0:
            if ops % 4 == 0:            # multiply
                stack[-1] *= n
            elif ops % 4 == 1:          # divide (truncate toward zero)
                a = stack[-1]
                stack[-1] = (abs(a) // n) * (1 if a >= 0 else -1)
            elif ops % 4 == 2:          # add
                stack.append(n)
            else:                       # subtract
                stack.append(-n)
            ops += 1
            n -= 1
        return sum(stack)
