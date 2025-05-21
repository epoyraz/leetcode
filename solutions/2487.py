class Solution:
    def partitionString(self, s):
        seen = set()
        ans = 0
        for c in s:
            if c in seen:
                ans += 1
                seen.clear()
            seen.add(c)
        return ans + 1
