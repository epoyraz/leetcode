class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.transform(s) == self.transform(t)
    
    def transform(self, s):
        mapping = {}
        res = []
        count = 0
        for c in s:
            if c not in mapping:
                mapping[c] = count
                count += 1
            res.append(mapping[c])
        return res
