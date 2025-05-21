class Solution(object):
    def minimumString(self, a, b, c):
        from itertools import permutations

        def merge(x, y):
            if y in x:
                return x
            max_overlap = 0
            for i in range(1, min(len(x), len(y)) + 1):
                if x[-i:] == y[:i]:
                    max_overlap = i
            return x + y[max_overlap:]

        res = None
        for p in permutations([a, b, c]):
            merged = merge(merge(p[0], p[1]), p[2])
            if res is None or len(merged) < len(res) or (len(merged) == len(res) and merged < res):
                res = merged
        return res
