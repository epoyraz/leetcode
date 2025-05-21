from collections import defaultdict

class Solution(object):
    def rootCount(self, edges, guesses, k):
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        guess_set = set((u, v) for u, v in guesses)
        res = [0]  # wrap in list for mutability

        def dfs(node, parent):
            count = 0
            for nei in tree[node]:
                if nei == parent:
                    continue
                if (node, nei) in guess_set:
                    count += 1
                count += dfs(nei, node)
            return count

        def reroot(node, parent, curr_count):
            if curr_count >= k:
                res[0] += 1
            for nei in tree[node]:
                if nei == parent:
                    continue
                delta = 0
                if (node, nei) in guess_set:
                    delta -= 1
                if (nei, node) in guess_set:
                    delta += 1
                reroot(nei, node, curr_count + delta)

        start_correct = dfs(0, -1)
        reroot(0, -1, start_correct)
        return res[0]
