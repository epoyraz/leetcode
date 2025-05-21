class Solution(object):
    def stringHash(self, s, k):
        result = ""
        for i in range(0, len(s), k):
            chunk = s[i:i + k]
            total = sum(ord(c) - ord('a') for c in chunk)
            hashed_char = chr((total % 26) + ord('a'))
            result += hashed_char
        return result
