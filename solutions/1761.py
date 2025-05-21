class Solution:
    def countVowelStrings(self, n):
        # The answer is C(n+4, 4): number of multisets of size n from 5 vowels.
        res = 1
        for i in range(1, 5):
            res = res * (n + i) // i
        return res
