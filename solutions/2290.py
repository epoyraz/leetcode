class Solution:
    def minimumRemoval(self, beans):
        beans.sort()
        total = sum(beans)
        res = float('inf')
        n = len(beans)
        for i, val in enumerate(beans):
            res = min(res, total - val * (n - i))
        return res
