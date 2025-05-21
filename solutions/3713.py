import itertools

class Solution(object):
    def supersequences(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 1) Gather all letters that appear and build a small index map 0..M-1
        letters = set()
        for w in words:
            letters.add(w[0])
            letters.add(w[1])
        letters = sorted(letters)
        M = len(letters)
        idx = {ch:i for i,ch in enumerate(letters)}
        
        # 2) Build adjacency list and detect self-loops
        adj = [[] for _ in range(M)]
        self_loop = [False]*M
        for u_ch, v_ch in words:
            u = idx[u_ch]
            v = idx[v_ch]
            adj[u].append(v)
            if u==v:
                self_loop[u] = True
        
        # 3) Required removals R = all self-loop nodes
        R_mask = 0
        for u in range(M):
            if self_loop[u]:
                R_mask |= (1<<u)
        
        # 4) Build list of âoptionalâ nodes V2 = those NOT already in R
        V2 = [u for u in range(M) if not (R_mask & (1<<u))]
        N2 = len(V2)
        
        # 5) A helper to test if G minus removed_mask is acyclic
        def is_acyclic(removed_mask):
            # compute indegree in the induced subgraph on V \ removed
            indeg = [0]*M
            for u in range(M):
                if removed_mask & (1<<u): 
                    continue
                for v in adj[u]:
                    if not (removed_mask & (1<<v)):
                        indeg[v] += 1
            # Kahnâs algorithm
            q = [u for u in range(M) 
                 if not (removed_mask & (1<<u)) and indeg[u]==0]
            seen = 0
            while q:
                u = q.pop()
                seen += 1
                for v in adj[u]:
                    if removed_mask & (1<<v): 
                        continue
                    indeg[v] -= 1
                    if indeg[v]==0:
                        q.append(v)
            # count of remaining nodes = M - popcount(removed_mask)
            return seen == (M - bin(removed_mask).count("1"))
        
        # 6) Find minimal extra removals S' â V2 so that RâªS' breaks all cycles
        best_k = None
        minimal_S_masks = []
        for k in range(N2+1):
            found_any = False
            for comb in itertools.combinations(range(N2), k):
                # build mask of these removed
                mask = R_mask
                for j in comb:
                    mask |= (1<<V2[j])
                if is_acyclic(mask):
                    found_any = True
                    minimal_S_masks.append(mask)
                # but we still need to collect **all** of size k,
                # so do *not* break here
            if found_any:
                best_k = k
                break
        
        # 7) For each minimal removal-mask, build the frequency array
        out = []
        for mask in minimal_S_masks:
            freq = [0]*26
            for i,ch in enumerate(letters):
                # if i in mask â we âremovedâ it from U1, so we need c=2; 
                # otherwise c=1
                freq[ord(ch)-97] = 2 if (mask & (1<<i)) else 1
            out.append(freq)
        
        return out
