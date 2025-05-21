from collections import defaultdict, deque

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        # Assign unique group ID to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Build graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topo_sort(nodes, graph, indegree):
            res = []
            q = deque([node for node in nodes if indegree[node] == 0])
            while q:
                u = q.popleft()
                res.append(u)
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            return res if len(res) == len(nodes) else []

        # Topo sort all items and all groups
        all_items = list(range(n))
        item_order = topo_sort(all_items, item_graph, item_indegree[:])
        if not item_order:
            return []

        all_groups = list(range(m))
        group_order = topo_sort(all_groups, group_graph, group_indegree[:])
        if not group_order:
            return []

        # Map group to items in topological order
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)

        # Assemble final result based on group order
        res = []
        for g in group_order:
            res.extend(group_to_items[g])

        return res
