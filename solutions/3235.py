class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        # build distance matrix for 26 letters
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            if w < dist[u][v]:
                dist[u][v] = w
        # Floyd-Warshall
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                di = dist[i]
                via = di[k]
                if via == INF: continue
                for j in range(26):
                    nd = via + dk[j]
                    if nd < di[j]:
                        di[j] = nd
        # sum up per-character conversions
        n = len(source)
        total = 0
        for i in range(n):
            s = ord(source[i]) - 97
            t = ord(target[i]) - 97
            if s == t:
                continue
            d = dist[s][t]
            if d >= INF:
                return -1
            total += d
        return total
