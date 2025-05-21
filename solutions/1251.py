class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        l, r = 0, n - 1
        l_sub, r_sub = "", ""
        count = 0

        for i in range(n):
            l_sub += text[i]
            r_sub = text[n - 1 - i] + r_sub
            if l_sub == r_sub:
                count += 1
                l_sub, r_sub = "", ""
        
        return count
