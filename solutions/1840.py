class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        from collections import defaultdict, Counter

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        n = len(source)
        parent = list(range(n))

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        res = 0
        for indices in groups.values():
            src_counter = Counter(source[i] for i in indices)
            tgt_counter = Counter(target[i] for i in indices)
            for val in tgt_counter:
                src_counter[val] -= tgt_counter[val]
            res += sum(max(0, v) for v in src_counter.values())

        return res
