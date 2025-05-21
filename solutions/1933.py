import re

class Solution(object):
    def numDifferentIntegers(self, word):
        parts = re.findall(r'\d+', word)
        seen = set()
        for p in parts:
            p = p.lstrip('0')
            if p == '':
                p = '0'
            seen.add(p)
        return len(seen)
