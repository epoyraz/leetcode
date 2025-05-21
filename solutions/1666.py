class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
