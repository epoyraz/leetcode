import collections

class Solution(object):
    def minCost(self, basket1, basket2):
        freq = collections.Counter(basket1)
        freq.update(basket2)
        for v, c in freq.iteritems():
            if c % 2:
                return -1

        freq1 = collections.Counter(basket1)
        freq2 = collections.Counter(basket2)
        surplus1, surplus2 = [], []
        for v in freq:
            d = freq1[v] - freq2[v]
            if d > 0:
                surplus1.extend([v] * (d // 2))
            elif d < 0:
                surplus2.extend([v] * ((-d) // 2))

        if not surplus1:
            return 0

        surplus1.sort()
        surplus2.sort(reverse=True)
        min_val = min(freq)
        cost = 0
        for x, y in zip(surplus1, surplus2):
            cost += min(x, y, 2 * min_val)
        return cost
