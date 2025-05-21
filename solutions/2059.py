class Solution(object):
    def countPalindromicSubsequence(self, s):
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        ans = 0
        for ch in first:
            i = first[ch]
            j = last[ch]
            if j - i < 2:
                continue
            seen = set()
            for k in range(i+1, j):
                seen.add(s[k])
            ans += len(seen)
        return ans
