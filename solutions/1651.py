class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [''] * len(s)
        for i, pos in enumerate(indices):
            res[pos] = s[i]
        return ''.join(res)
