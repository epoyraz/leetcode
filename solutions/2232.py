class Solution:
    def addSpaces(self, s, spaces):
        space_set = set(spaces)
        result = []

        for i, ch in enumerate(s):
            if i in space_set:
                result.append(' ')
            result.append(ch)

        return ''.join(result)
