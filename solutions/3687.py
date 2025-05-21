import sys
sys.setrecursionlimit(10**7)
from collections import deque

class Solution(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums:   List[int]
        :rtype:       List[int]
        """
        n = len(nums)
        # 1) Build undirected adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # 2) Root the tree at 0 with a BFS: record parent, depth, and children[]
        parent   = [-1] * n
        parent[0] = 0
        depth    = [0] * n
        children = [[] for _ in range(n)]
        dq = deque([0])
        while dq:
            u = dq.popleft()
            for v, w in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    depth[v]  = depth[u] + w
                    children[u].append(v)
                    dq.append(v)

        # 3) State for our DFS + sliding window:
        path_nodes     = []    # stack of node-ids on the rootâu path
        dist_prefix    = []    # dist_prefix[i] = depth[path_nodes[i]]
        last_occurrence = {}   # maps value â last index in path_nodes

        # wrap scalars in lists so we can mutate them inside dfs()
        start_idx    = [0]
        ans_length   = [0]
        ans_node_cnt = [1]      # even a single node (0âlength path) counts

        def dfs(u):
            idx = len(path_nodes)
            prev_start = start_idx[0]
            prev_last  = last_occurrence.get(nums[u], None)

            # push u
            path_nodes.append(u)
            dist_prefix.append(depth[u])

            # if we saw nums[u] in the current window, slide start up
            if prev_last is not None and prev_last >= start_idx[0]:
                start_idx[0] = prev_last + 1
            last_occurrence[nums[u]] = idx

            # compute specialâpath length & node count
            cur_len = dist_prefix[idx] - dist_prefix[start_idx[0]]
            cur_cnt = idx - start_idx[0] + 1
            # update global best
            if (cur_len > ans_length[0]) or \
               (cur_len == ans_length[0] and cur_cnt < ans_node_cnt[0]):
                ans_length[0]   = cur_len
                ans_node_cnt[0] = cur_cnt

            # recurse to children
            for v in children[u]:
                dfs(v)

            # backtrack
            path_nodes.pop()
            dist_prefix.pop()
            if prev_last is None:
                del last_occurrence[nums[u]]
            else:
                last_occurrence[nums[u]] = prev_last
            start_idx[0] = prev_start

        # kick off
        dfs(0)
        return [ans_length[0], ans_node_cnt[0]]
