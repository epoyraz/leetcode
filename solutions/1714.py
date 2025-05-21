class Solution(object):
    def reorderSpaces(self, text):
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * spaces
        gaps = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)
        return (' ' * gaps).join(words) + ' ' * extra
