from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        res = []
        p_count = Counter(p)
        s_count = Counter()
        n, m = len(s), len(p)
        
        for i in range(n):
            s_count[s[i]] += 1
            if i >= m:
                s_count[s[i - m]] -= 1
                if s_count[s[i - m]] == 0:
                    del s_count[s[i - m]]
            if s_count == p_count:
                res.append(i - m + 1)
        
        return res
