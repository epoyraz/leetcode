import sys
sys.setrecursionlimit(10**7)

class Solution:
    def componentValue(self, nums, edges):
        n = len(nums)
        # Build adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # Root at 0
        parent = [-1] * n
        children = [[] for _ in range(n)]
        stack = [0]
        parent[0] = 0
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for w in adj[u]:
                if parent[w] < 0:
                    parent[w] = u
                    children[u].append(w)
                    stack.append(w)
        S = sum(nums)
        # All divisors of S
        divs = []
        i = 1
        while i * i <= S:
            if S % i == 0:
                divs.append(i)
                if i * i != S:
                    divs.append(S // i)
            i += 1
        divs.sort()
        # Try each piece-sum t
        def can_split(t):
            target = t
            count = 0
            subsum = [0] * n
            for u in reversed(order):
                s = nums[u]
                for w in children[u]:
                    s += subsum[w]
                if s == target:
                    count += 1
                    subsum[u] = 0
                elif s < target:
                    subsum[u] = s
                else:
                    return False
            return count == S // t

        for t in divs:
            if can_split(t):
                return S // t - 1
        return 0
