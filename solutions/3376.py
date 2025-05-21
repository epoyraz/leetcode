class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        # 1) Build reversedâTrie with âbestâ index at each node.
        # Each node: { children: dict, best_idx: int, best_len: int }
        root = {"children": {}, "best_idx": None, "best_len": float("inf")}
        
        # Helper to try updating a nodeâs best_* given word at index i
        def consider(node, length, idx):
            # better if shorter-length, or same length but earlier index
            if length < node["best_len"] or (
               length == node["best_len"] and idx < node["best_idx"]
            ):
                node["best_len"] = length
                node["best_idx"] = idx
        
        # First, consider all words at the root (this handles suffix-length=0)
        for i, w in enumerate(wordsContainer):
            consider(root, len(w), i)
        
        # Insert each container word in reversed order
        for i, w in enumerate(wordsContainer):
            node = root
            for ch in reversed(w):
                if ch not in node["children"]:
                    node["children"][ch] = {
                        "children": {},
                        "best_idx": None,
                        "best_len": float("inf")
                    }
                node = node["children"][ch]
                consider(node, len(w), i)
        
        # 2) For each query, walk the reversed Trie as far as possible
        ans = []
        for q in wordsQuery:
            node = root
            best = node["best_idx"]
            for ch in reversed(q):
                if ch in node["children"]:
                    node = node["children"][ch]
                    best = node["best_idx"]
                else:
                    break
            ans.append(best)
        
        return ans
