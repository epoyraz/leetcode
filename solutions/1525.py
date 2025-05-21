class Solution(object):
    def processQueries(self, queries, m):
        P = list(range(1, m + 1))
        result = []

        for q in queries:
            idx = P.index(q)
            result.append(idx)
            P.pop(idx)
            P.insert(0, q)

        return result
