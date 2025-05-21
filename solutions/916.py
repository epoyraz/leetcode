class Solution(object):
    def decodeAtIndex(self, s, k):
        size = 0

        # First pass: compute the total length of the decoded string
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        # Second pass: work backwards to find the k-th character
        for i in reversed(range(len(s))):
            ch = s[i]
            k %= size
            if k == 0 and ch.isalpha():
                return ch
            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1
