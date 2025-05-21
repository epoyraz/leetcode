class Solution:
    def removePalindromeSub(self, s):
        # If the entire string is already a palindrome, 1 step suffices.
        if s == s[::-1]:
            return 1
        # Otherwise, we can do it in 2 steps (remove all 'a's then all 'b's).
        return 2
