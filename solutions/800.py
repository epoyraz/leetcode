class Solution(object):
    def letterCasePermutation(self, s):
        res = []
        
        def dfs(path, i):
            if i == len(s):
                res.append(path)
                return
            if s[i].isalpha():
                dfs(path + s[i].lower(), i + 1)
                dfs(path + s[i].upper(), i + 1)
            else:
                dfs(path + s[i], i + 1)
        
        dfs("", 0)
        return res
