class Solution(object):
    def countVisitedNodes(self, edges):
        n = len(edges)
        ans = [0] * n
        state = [0] * n  # 0=unvisited,1=visiting,2=done
        for i in range(n):
            if state[i] != 0:
                continue
            path = []
            node = i
            while True:
                state[node] = 1
                path.append(node)
                nxt = edges[node]
                if state[nxt] == 0:
                    node = nxt
                    continue
                # found a back-edge or to completed
                if state[nxt] == 1:
                    # cycle detected
                    idx = path.index(nxt)
                    cycle_len = len(path) - idx
                    for j in range(idx, len(path)):
                        ans[path[j]] = cycle_len
                    # nodes before cycle
                    for j in range(idx-1, -1, -1):
                        ans[path[j]] = ans[path[j+1]] + 1
                else:
                    # nxt already done
                    for j in range(len(path)-1, -1, -1):
                        ans[path[j]] = ans[edges[path[j]]] + 1
                break
            # mark all on path as done
            for node in path:
                state[node] = 2
        return ans