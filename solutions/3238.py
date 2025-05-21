class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        n = len(source)
        # group operations by length
        from collections import defaultdict
        ops_by_len = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            L = len(o)
            ops_by_len[L].append((o, c, w))
        
        # rolling-hash parameters
        base = 91138233
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        
        # precompute powers
        pow1 = [1] * (n+1)
        pow2 = [1] * (n+1)
        for i in range(1, n+1):
            pow1[i] = (pow1[i-1] * base) % mod1
            pow2[i] = (pow2[i-1] * base) % mod2
        
        # prefix hashes for source and target
        h1_s = [0] * (n+1)
        h2_s = [0] * (n+1)
        h1_t = [0] * (n+1)
        h2_t = [0] * (n+1)
        for i, ch in enumerate(source, 1):
            v = ord(ch)
            h1_s[i] = (h1_s[i-1] * base + v) % mod1
            h2_s[i] = (h2_s[i-1] * base + v) % mod2
        for i, ch in enumerate(target, 1):
            v = ord(ch)
            h1_t[i] = (h1_t[i-1] * base + v) % mod1
            h2_t[i] = (h2_t[i-1] * base + v) % mod2
        
        # helper to get double-hash of substring [i:j)
        def sub_hash(h1, h2, i, j):
            x1 = (h1[j] - h1[i] * pow1[j-i]) % mod1
            x2 = (h2[j] - h2[i] * pow2[j-i]) % mod2
            return (x1, x2)
        
        INF = 10**30
        # for each length L, build graph and floyd-warshall all-pairs distances
        dist_by_len = {}
        hash_to_idx = {}
        for L, ops in ops_by_len.items():
            # collect all distinct node strings of length L
            nodes = {}
            idx = 0
            for o, c, _ in ops:
                if o not in nodes:
                    nodes[o] = idx; idx += 1
                if c not in nodes:
                    nodes[c] = idx; idx += 1
            N = idx
            # initialize dist matrix
            dist = [[INF]*N for _ in range(N)]
            for i in range(N):
                dist[i][i] = 0
            # add edges
            for o, c, w in ops:
                u = nodes[o]
                v = nodes[c]
                if w < dist[u][v]:
                    dist[u][v] = w
            # floyd-warshall
            for k in range(N):
                dk = dist[k]
                for i in range(N):
                    di = dist[i]
                    via = di[k]
                    if via == INF: continue
                    # unroll inner
                    for j in range(N):
                        nd = via + dk[j]
                        if nd < di[j]:
                            di[j] = nd
            # build hash->idx map for substrings of length L
            hmap = {}
            # compute hash for each node string
            for s_str, i_node in nodes.items():
                h1 = 0
                h2 = 0
                for ch in s_str:
                    v = ord(ch)
                    h1 = (h1 * base + v) % mod1
                    h2 = (h2 * base + v) % mod2
                hmap[(h1,h2)] = i_node
            dist_by_len[L] = dist
            hash_to_idx[L] = hmap
        
        # DP over prefix
        dp = [INF] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            # trivial single char match
            if source[i-1] == target[i-1]:
                if dp[i-1] < dp[i]:
                    dp[i] = dp[i-1]
            # try each op-length segment ending at i
            for L, dist in dist_by_len.items():
                if L > i: 
                    continue
                j = i - L
                # get substring hashes
                hs = sub_hash(h1_s, h2_s, j, i)
                ht = sub_hash(h1_t, h2_t, j, i)
                hmap = hash_to_idx[L]
                u = hmap.get(hs)
                if u is None:
                    continue
                v = hmap.get(ht)
                if v is None:
                    continue
                d = dist[u][v]
                if d < INF:
                    cost_here = dp[j] + d
                    if cost_here < dp[i]:
                        dp[i] = cost_here
        
        return dp[n] if dp[n] < INF else -1
