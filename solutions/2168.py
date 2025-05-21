class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tokens = s.split()
        prev = -1
        for token in tokens:
            if token.isdigit():
                num = int(token)
                if num <= prev:
                    return False
                prev = num
        return True
