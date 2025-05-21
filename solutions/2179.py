import bisect

class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort(key=lambda x: x[0])
        prices = [p for p, _ in items]
        max_b = []
        curr = 0
        for _, b in items:
            curr = curr if curr > b else b
            max_b.append(curr)
        ans = []
        for q in queries:
            i = bisect.bisect_right(prices, q) - 1
            ans.append(max_b[i] if i >= 0 else 0)
        return ans
