class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        l = s + "#" + rev_s
        table = [0] * len(l)

        for i in range(1, len(l)):
            j = table[i - 1]
            while j > 0 and l[i] != l[j]:
                j = table[j - 1]
            if l[i] == l[j]:
                j += 1
            table[i] = j

        return rev_s[:len(s) - table[-1]] + s
