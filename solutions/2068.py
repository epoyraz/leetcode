# Definition of the trie node for bitwise operations
class TrieNode(object):
    def __init__(self):
        self.child0 = None
        self.child1 = None
        self.count = 0

class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        import sys
        sys.setrecursionlimit(10**7)

        n = len(parents)
        # Build adjacency list and find root
        children = [[] for _ in range(n)]
        root = -1
        for v, p in enumerate(parents):
            if p == -1:
                root = v
            else:
                children[p].append(v)

        # Group queries by node
        qs = [[] for _ in range(n)]
        for i, (node, val) in enumerate(queries):
            qs[node].append((i, val))

        ans = [0] * len(queries)

        # Parameters for our bitwise trie
        MAXB = 18  # enough for values up to ~2*10^5

        # Initialize the trie
        trie_root = TrieNode()

        # Insert x into the trie
        def trie_insert(x):
            node = trie_root
            node.count += 1
            for b in range(MAXB - 1, -1, -1):
                bit = (x >> b) & 1
                if bit == 0:
                    if not node.child0:
                        node.child0 = TrieNode()
                    node = node.child0
                else:
                    if not node.child1:
                        node.child1 = TrieNode()
                    node = node.child1
                node.count += 1

        # Delete x from the trie
        def trie_delete(x):
            node = trie_root
            node.count -= 1
            for b in range(MAXB - 1, -1, -1):
                bit = (x >> b) & 1
                if bit == 0:
                    node = node.child0
                else:
                    node = node.child1
                node.count -= 1

        # Query max XOR with x over all values in the trie
        def trie_max_xor(x):
            node = trie_root
            res = 0
            for b in range(MAXB - 1, -1, -1):
                bit = (x >> b) & 1
                # prefer opposite bit if available
                if bit == 0:
                    if node.child1 and node.child1.count > 0:
                        res |= (1 << b)
                        node = node.child1
                    else:
                        node = node.child0
                else:
                    if node.child0 and node.child0.count > 0:
                        res |= (1 << b)
                        node = node.child0
                    else:
                        node = node.child1
            return res

        # DFS to maintain the trie along the rootâcurrent path
        def dfs(u):
            # insert this node's value
            trie_insert(u)
            # answer this node's queries
            for qi, qv in qs[u]:
                ans[qi] = trie_max_xor(qv)
            # recurse children
            for v in children[u]:
                dfs(v)
            # on backtrack, remove this node's value
            trie_delete(u)

        # run DFS from the root
        dfs(root)
        return ans
