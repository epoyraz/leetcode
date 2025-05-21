from collections import Counter

class Solution:
    def minSteps(self, s, t):
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        # We need to make up the deficit in t for each character
        return sum(max(0, cnt_s[ch] - cnt_t[ch]) for ch in cnt_s)
