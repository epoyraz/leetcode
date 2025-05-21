class Solution:
    def greatestLetter(self, s):
        lowers = set()
        uppers = set()
        for ch in s:
            if 'a' <= ch <= 'z':
                lowers.add(ch)
            else:
                uppers.add(ch)
        
        # Check from 'Z' down to 'A'
        for code in range(ord('Z'), ord('A') - 1, -1):
            ch = chr(code)
            if ch in uppers and ch.lower() in lowers:
                return ch
        return ""
