from collections import defaultdict

class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        # Build the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = [0] * n

        def dfs(node, parent):
            counter = [0] * 26  # label counts in subtree

            label_index = ord(labels[node]) - ord('a')
            counter[label_index] = 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_counter = dfs(neighbor, node)
                for i in range(26):
                    counter[i] += child_counter[i]

            ans[node] = counter[label_index]
            return counter

        dfs(0, -1)
        return ans
