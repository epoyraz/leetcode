class Solution(object):
    def minCost(self, n, cost):
        """
        :type n:   int        (even)
        :type cost: List[List[int]]  # n Ã 3
        :rtype:     int
        """
        M = n // 2
        # Build the two rows:
        #  P1[i] = cost[i]
        #  Q[i] = cost[n-1-i]
        cost_P1 = cost[:M]
        cost_Q  = [cost[n-1-i] for i in range(M)]
        
        # All valid (c1,c2) with c1!=c2:
        states = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
        
        # Precompute, for each state s, which previous-state indices t
        # satisfy t[0]!=c1 and t[1]!=c2.
        prev_states = []
        for (c1,c2) in states:
            ok = []
            for ti,(p1,p2) in enumerate(states):
                if p1 != c1 and p2 != c2:
                    ok.append(ti)
            prev_states.append(ok)
        
        # dp_prev[s] = min cost up through column i-1 ending in state s
        # Initialize for column 0:
        dp_prev = [
            cost_P1[0][c1] + cost_Q[0][c2]
            for (c1,c2) in states
        ]
        
        # Sweep columns 1..M-1
        for i in range(1, M):
            dp_cur = [10**30]*6
            for si,(c1,c2) in enumerate(states):
                base = cost_P1[i][c1] + cost_Q[i][c2]
                # transition only from those prev states where
                # P1[i]!=P1[i-1] and Q[i]!=Q[i-1]
                best_prev = min(dp_prev[t] for t in prev_states[si])
                dp_cur[si] = base + best_prev
            dp_prev = dp_cur
        
        # Answer is the minimum over finalâcolumn states
        return min(dp_prev)
