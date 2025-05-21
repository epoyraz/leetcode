class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(ord('A') + columnNumber % 26) + result
            columnNumber //= 26
        return result
