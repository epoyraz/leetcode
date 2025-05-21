class Solution(object):
    def toLowerCase(self, s):
        res = []
        for c in s:
            if 'A' <= c <= 'Z':
                # convert uppercase to lowercase by ASCII offset
                res.append(chr(ord(c) - ord('A') + ord('a')))
            else:
                res.append(c)
        return ''.join(res)
