class Solution(object):
    def deleteDuplicateFolder(self, paths):
        # Build folder tree with a dummy root
        class Node(object):
            __slots__ = ("children", "sig")
            def __init__(self):
                self.children = {}
                self.sig = None

        root = Node()
        for p in paths:
            cur = root
            for name in p:
                if name not in cur.children:
                    cur.children[name] = Node()
                cur = cur.children[name]

        # Map subtree signature (tuple of (name, sig)) -> unique ID
        sig2id = {}
        next_id = [1]   # use list to mutate inside nested function
        from collections import Counter
        cnt = Counter()

        # Post-order: compute signature ID for each node
        def dfs_sig(node):
            items = []
            for name, child in node.children.items():
                dfs_sig(child)
                items.append((name, child.sig))
            if not items:
                # leaf folder
                node.sig = 0
            else:
                items.sort()
                key = tuple(items)
                sid = sig2id.get(key)
                if sid is None:
                    sid = next_id[0]
                    sig2id[key] = sid
                    next_id[0] += 1
                node.sig = sid
                cnt[sid] += 1

        dfs_sig(root)

        res = []
        path = []

        # Pre-order: collect paths of non-deleted folders
        def dfs_collect(node):
            # skip (delete) if non-root, non-leaf, and signature repeats
            if node is not root and node.sig != 0 and cnt[node.sig] > 1:
                return
            # record this folder (except dummy root)
            if node is not root:
                res.append(path[:])
            for name, child in node.children.items():
                path.append(name)
                dfs_collect(child)
                path.pop()

        dfs_collect(root)
        return res
