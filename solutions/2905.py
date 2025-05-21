class Solution(object):
    def countPalindromePaths(self, parent, s):
        n = len(parent)

        # build adjacency with the character on each edge
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            adj[p].append((i, ord(s[i]) - 97))     # store child and letter-index (0â25)

        # depth-first traversal to compute parity-masks from root to every node
        masks = [0] * n
        stack = [(0, 0)]                            # (node, mask)
        while stack:
            node, mask = stack.pop()
            masks[node] = mask
            for child, ch_idx in adj[node]:
                stack.append((child, mask ^ (1 << ch_idx)))

        # count pairs whose XOR of masks has â¤1 bit set
        from collections import defaultdict
        freq = defaultdict(int)                     # mask -> how many times seen so far
        ans = 0
        for m in masks:
            ans += freq[m]                          # XOR == 0  â all counts even
            for j in range(26):                     # XOR differs in exactly one bit
                ans += freq[m ^ (1 << j)]
            freq[m] += 1

        return ans
