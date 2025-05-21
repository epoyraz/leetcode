class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for c in s:
            if c == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # remove '('
                stack.extend(temp)
            else:
                stack.append(c)
        return ''.join(stack)
