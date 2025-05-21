class Solution(object):
    def removeStars(self, s):
        stack = []
        for c in s:
            if c != '*':
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
