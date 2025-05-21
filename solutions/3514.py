class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        n â¤ 1e5 , q â¤ 1e5
        time   :  O( n + q Â· Î±(n) )      (Î± = inverse Ackermann â 4)
        memory :  O( n )
        """

        # ------------------------------------------------------------------
        #  Disjoint-set of *interval starts*
        #    parent[i]   â representative (leftmost start) of the interval
        #    end[i]      â right end of that interval     (only valid for rep)
        #    next_start[i] â the next *start index* to the right (or n)
        #
        #  Initially we have chain edges only:
        #     intervals 0â1, 1â2, â¦, n-2ân-1       (n-1 intervals)
        # ------------------------------------------------------------------
        parent      = list(range(n))             # DSU parent
        end         = [i + 1 for i in range(n)]  # right ends
        end[-1]     = n - 1                      # last city has no edge
        next_start  = [i + 1 for i in range(n)]  # linked list of starts
        next_start[-1] = n                       # sentinel

        # `reach[u]` = furthest city that *node u* can reach in one edge
        reach = end[:]                           # start with the chain edges

        intervals = n - 1                        # current path length

        # ---------- DSU find with path-compression -------------------------
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # ---------- next live interval start to the right of x -------------
        def next_live(x):
            y = next_start[x]
            while y < n and parent[y] != y:      # skip deleted starts
                next_start[x] = next_start[y]    # path-compression
                y = next_start[x]
            return y                             # n means ânoneâ

        # ---------------------- process every query ------------------------
        ans = []
        for u, v in queries:

            # 1. If the shortcut does not improve reach[u] â nothing changes
            if v <= reach[u]:
                ans.append(intervals)
                continue
            reach[u] = v                         # store the new edge

            # 2. Locate the interval that *contains* u  (its representative)
            s = find(u)

            # 3. If the shortcut ends inside the same interval, only extend
            #    its right end; the number of intervals is unchanged.
            if v <= end[s]:
                end[s] = v
                ans.append(intervals)
                continue

            # 4. Extend the intervalâs right end to v and
            #    *merge* every following interval whose start < new end.
            end[s] = v
            t = next_live(s)
            while t < n and t < end[s]:
                #   merge interval t into s
                end[s]      = max(end[s], end[t])
                parent[t]   = s
                next_start[s] = next_start[t]    # splice t out of the list
                intervals  -= 1                  # one interval disappears
                t = next_live(s)                 # continue to the next start

            ans.append(intervals)

        return ans
