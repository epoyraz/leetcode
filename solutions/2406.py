class Solution:
    def decodeMessage(self, key, message):
        mapping = {}
        current = 'a'

        for char in key:
            if char != ' ' and char not in mapping:
                mapping[char] = current
                current = chr(ord(current) + 1)

        return ''.join(mapping[c] if c in mapping else ' ' for c in message)
