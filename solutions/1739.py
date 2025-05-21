class Solution:
    def check(self, a, b):
        l, r = 0, len(a) - 1
        # Move inward while the mixed ends match
        while l < r and a[l] == b[r]:
            l += 1
            r -= 1
        # If we've crossed, the mix is already a palindrome
        if l >= r:
            return True
        # Otherwise, check the remainder in either original string
        return self.is_pal(a, l, r) or self.is_pal(b, l, r)

    def is_pal(self, s, i, j):
        # Standard palindrome check on s[i..j]
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def checkPalindromeFormation(self, a, b):
        # Try aprefix + bsuffix or bprefix + asuffix
        return self.check(a, b) or self.check(b, a)
