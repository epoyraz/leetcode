class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(prefix, last):
            if len(prefix) == n:
                res.append(prefix)
                return
            # always can add '1'
            dfs(prefix + '1', '1')
            # add '0' only if last wasn't '0'
            if last != '0':
                dfs(prefix + '0', '0')
        
        # start with first char '0' or '1'
        dfs("0", "0")
        dfs("1", "1")
        return res
