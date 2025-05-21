class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch.isdigit():
                # remove the closest non-digit to the left
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
