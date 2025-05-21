from collections import defaultdict

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        parent = list(range(len(s)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        # Step 1: Union connected indices
        for a, b in pairs:
            union(a, b)

        # Step 2: Group characters by connected component
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)

        res = list(s)
        for indices in groups.values():
            chars = sorted([s[i] for i in indices])
            for i, ch in zip(sorted(indices), chars):
                res[i] = ch

        return ''.join(res)
