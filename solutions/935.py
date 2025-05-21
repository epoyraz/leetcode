class Solution:
    def orderlyQueue(self, s, k):
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return ''.join(sorted(s))
