class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        total = 0
        res = []

        for i in range(n-1, -1, -1):
            total = (total + shifts[i]) % 26
            new_char = chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))
            res.append(new_char)

        return ''.join(reversed(res))
