class Solution(object):
    def nextGreaterElement(self, n):
        s = list(str(n))
        # 1. find the pivot
        i = len(s) - 2
        while i >= 0 and s[i] >= s[i+1]:
            i -= 1
        if i < 0:
            return -1
        # 2. find the rightmost successor to pivot
        j = len(s) - 1
        while s[j] <= s[i]:
            j -= 1
        # 3. swap pivot and successor
        s[i], s[j] = s[j], s[i]
        # 4. reverse the suffix
        s[i+1:] = reversed(s[i+1:])
        res = int("".join(s))
        # 5. check 32-bit limit
        return res if res <= 2**31 - 1 else -1
