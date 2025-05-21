import heapq

class Solution(object):
    def minOperations(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # 1) If either n or m is prime, impossible.
        def sieve(N):
            is_prime = [False, False] + [True]*(N-1)
            for p in range(2, int(N**0.5)+1):
                if is_prime[p]:
                    for q in range(p*p, N+1, p):
                        is_prime[q] = False
            return is_prime

        ds = str(n)
        if len(str(m)) != len(ds):
            return -1
        
        D = len(ds)
        MAX = 10**D - 1
        is_prime = sieve(MAX)

        if is_prime[n] or is_prime[m]:
            return -1

        # 2) Dijkstra's over [10^(D-1) .. 10^D - 1], skipping primes.
        INF = 10**18
        dist = [INF] * (MAX+1)
        dist[n] = n
        pq = [(n, n)]  # (distance, node)

        while pq:
            d_u, u = heapq.heappop(pq)
            if d_u > dist[u]:
                continue
            if u == m:
                return d_u
            # generate neighbors by digit Â±1
            s = list(str(u))
            for i in range(D):
                orig = int(s[i])
                for delta in (-1, +1):
                    nd = orig + delta
                    # keep digit in [0..9], and preserve D-digit length
                    if nd < 0 or nd > 9:
                        continue
                    if i == 0 and nd == 0:
                        continue
                    s[i] = str(nd)
                    v = int("".join(s))
                    s[i] = str(orig)
                    # only non-prime nodes allowed
                    if not is_prime[v]:
                        ndist = d_u + v
                        if ndist < dist[v]:
                            dist[v] = ndist
                            heapq.heappush(pq, (ndist, v))

        return -1
