class Solution:
    def longestValidSubstring(self, word, forbidden):
        forbidden_by_len = {}
        for f in forbidden:
            forbidden_by_len.setdefault(len(f), set()).add(f)
        
        n = len(word)
        start = 0
        best = 0
        
        for r in range(n):
            for L in range(1, min(10, r + 1) + 1):
                if L in forbidden_by_len:
                    sub = word[r - L + 1 : r + 1]
                    if sub in forbidden_by_len[L]:
                        start = max(start, r - L + 2)
            best = max(best, r - start + 1)
        
        return best
