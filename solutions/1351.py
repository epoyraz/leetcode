from collections import Counter

class Solution:
    def balancedString(self, s):
        n = len(s)
        count = Counter(s)
        target = n // 4
        if all(count[c] == target for c in "QWER"):
            return 0

        left = 0
        res = n
        for right in range(n):
            count[s[right]] -= 1
            while left < n and all(count[c] <= target for c in "QWER"):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res
