from collections import deque, defaultdict

class Solution:
    def countPaths(self, n, edges):
        # 1) Sieve primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        # 2) Build adjacency list
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 3) Find connected components of the forest after removing primes
        comp_id = [0] * (n + 1)      # component id for each non-prime node
        comp_size = []               # comp_size[c] = size of component c
        visited = [False] * (n + 1)

        cid = 0
        for u in range(1, n + 1):
            if not is_prime[u] and not visited[u]:
                # BFS/DFS from u over non-prime nodes
                cid += 1
                size = 0
                dq = deque([u])
                visited[u] = True
                comp_id[u] = cid
                while dq:
                    x = dq.popleft()
                    size += 1
                    for w in g[x]:
                        if not is_prime[w] and not visited[w]:
                            visited[w] = True
                            comp_id[w] = cid
                            dq.append(w)
                comp_size.append(size)  # comp_size[cid-1] = size

        # 4) For each prime p, gather sizes of adjacent non-prime components
        ans = 0
        for p in range(1, n + 1):
            if not is_prime[p]:
                continue
            # collect sizes of each distinct non-prime component neighbor
            sizes = []
            for v in g[p]:
                if not is_prime[v]:
                    c = comp_id[v] - 1
                    sizes.append(comp_size[c])
            if not sizes:
                continue

            S = sum(sizes)
            S2 = sum(s * s for s in sizes)
            # sum over i<j of s_i * s_j = (S^2 - S2) // 2
            pairs_between_comps = (S * S - S2) // 2
            pairs_with_p = S
            ans += pairs_between_comps + pairs_with_p

        return ans
