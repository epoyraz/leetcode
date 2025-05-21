class Solution(object):
    def edgeScore(self, edges):
        from collections import defaultdict

        score = defaultdict(int)
        for i, v in enumerate(edges):
            score[v] += i

        max_score = -1
        result = -1

        for node in range(len(edges)):
            if score[node] > max_score or (score[node] == max_score and node < result):
                max_score = score[node]
                result = node

        return result
