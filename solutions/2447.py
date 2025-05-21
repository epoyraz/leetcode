class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        from collections import defaultdict

        weight_map = defaultdict(int)

        for v, w in items1:
            weight_map[v] += w
        for v, w in items2:
            weight_map[v] += w

        return sorted([[v, weight_map[v]] for v in weight_map])
