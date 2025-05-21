class Solution:
    def breakPalindrome(self, palindrome):
        n = len(palindrome)
        if n == 1:
            return ""
        s = list(palindrome)
        # Try to change the first non-'a' in the first half to 'a'
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return "".join(s)
        # If all first half are 'a', change the last character to 'b'
        s[-1] = 'b'
        return "".join(s)
