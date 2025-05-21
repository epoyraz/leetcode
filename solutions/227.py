class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        stack = []
        num = 0
        sign = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / float(num))
                sign = ch
                num = 0
        
        return sum(stack)
