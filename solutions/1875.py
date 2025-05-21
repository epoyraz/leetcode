from collections import defaultdict
import sys
sys.setrecursionlimit(1 << 20)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Precompute coprime relations
        coprime_map = [[] for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    coprime_map[i].append(j)

        # Map from num -> list of (depth, node)
        ancestors = defaultdict(list)
        ans = [-1] * n

        def dfs(node, parent, depth):
            max_depth = -1
            best_ancestor = -1

            # Check all coprime candidates
            for val in coprime_map[nums[node]]:
                if ancestors[val]:
                    d, anc = ancestors[val][-1]
                    if d > max_depth:
                        max_depth = d
                        best_ancestor = anc

            ans[node] = best_ancestor

            # Push current node into ancestor stack
            ancestors[nums[node]].append((depth, node))

            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node, depth + 1)

            # Backtrack
            ancestors[nums[node]].pop()

        dfs(0, -1, 0)
        return ans
