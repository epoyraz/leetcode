class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(s, t):
            it = iter(t)
            return all(c in it for c in s)
        
        strs.sort(key=len, reverse=True)
        
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)
        
        return -1
