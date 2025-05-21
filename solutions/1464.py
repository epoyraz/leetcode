from collections import Counter

class Solution:
    def minSetSize(self, arr):
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        removed = 0
        target = len(arr) // 2
        ans = 0
        for c in counts:
            removed += c
            ans += 1
            if removed >= target:
                return ans
        return ans
