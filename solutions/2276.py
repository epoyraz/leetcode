class Solution:
    def groupStrings(self, words):
        from collections import defaultdict

        def word_to_mask(word):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        parent = {}
        size = defaultdict(int)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
                size[px] += size[py]

        masks = set()
        for word in words:
            m = word_to_mask(word)
            masks.add(m)
            parent[m] = m
            size[m] += 1

        for m in list(masks):
            # Try removing each letter
            for i in range(26):
                if (m >> i) & 1:
                    m2 = m ^ (1 << i)
                    if m2 in parent:
                        union(m, m2)

            # Try replacing each letter (remove + add)
            for i in range(26):
                if (m >> i) & 1:
                    m_removed = m ^ (1 << i)
                    for j in range(26):
                        if not (m_removed >> j) & 1:
                            m2 = m_removed | (1 << j)
                            if m2 in parent:
                                union(m, m2)

        groups = set(find(m) for m in masks)
        max_size = max(size[find(m)] for m in masks)
        return [len(groups), max_size]
