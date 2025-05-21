class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        for ch in counter:
            if counter[ch] < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))
        
        return len(s)
