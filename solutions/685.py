class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = [0] * (n + 1)
        cand1 = cand2 = None

        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break

        def find(u, par):
            if par[u] != u:
                par[u] = find(par[u], par)
            return par[u]

        def union(u, v, par):
            pu, pv = find(u, par), find(v, par)
            if pu == pv:
                return False
            par[pu] = pv
            return True

        if not cand1:
            par = [i for i in range(n + 1)]
            for u, v in edges:
                if not union(u, v, par):
                    return [u, v]
        else:
            for cand in [cand2, cand1]:
                par = [i for i in range(n + 1)]
                for u in range(1, n + 1):
                    parent[u] = u
                valid = True
                for u, v in edges:
                    if [u, v] == cand:
                        continue
                    if not union(u, v, par):
                        valid = False
                        break
                if valid:
                    return cand
