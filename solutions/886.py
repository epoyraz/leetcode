class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)
        return stack[0]
