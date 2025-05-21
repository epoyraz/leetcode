class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        delta = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                delta[start] += 1
                delta[end + 1] -= 1
            else:
                delta[start] -= 1
                delta[end + 1] += 1

        for i in range(1, n):
            delta[i] += delta[i - 1]

        res = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + delta[i]) % 26
            res.append(chr(ord('a') + shift))

        return ''.join(res)
