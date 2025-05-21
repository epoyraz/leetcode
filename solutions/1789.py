from collections import deque

class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        n = len(boxes)
        # 1) build prefixâsums of weight W[i] and portâchanges P[i]
        W = [0] * (n+1)
        P = [0] * (n+1)
        for i in range(1, n+1):
            port, wt = boxes[i-1]
            W[i] = W[i-1] + wt
            if i > 1 and port != boxes[i-2][0]:
                P[i] = P[i-1] + 1
            else:
                P[i] = P[i-1]

        INF = 10**18
        dp = [INF] * (n+1)
        dp[0] = 0

        # f[l] = dp[l-1] - P[l]; 
        # we store candidate l's in deque, increasing by f[l].
        deq = deque()
        # initial candidate l = 1
        # f[1] = dp[0] - P[1] = 0 - 0 = 0
        deq.append(1)

        wl = 0  # pointer for weightâconstraint

        for r in range(1, n+1):
            # advance wl so that W[wl] >= W[r] - maxWeight
            while wl < r and W[wl] < W[r] - maxWeight:
                wl += 1

            # leftmost valid l must satisfy:
            #   l >= wl+1  (weight)
            #   l >= r-maxBoxes+1  (count)
            L = max(wl+1, r - maxBoxes + 1, 1)

            # pop off any l < L
            while deq and deq[0] < L:
                deq.popleft()

            # if there's no valid batch-start, dp[r] stays INF
            if deq:
                best_l = deq[0]
                # dp[r] = min over l of dp[l-1] + (2 + P[r] - P[l])
                dp[r] = 2 + P[r] + (dp[best_l-1] - P[best_l])

            # prepare candidate l = r+1 for future r's
            if r < n and dp[r] < INF:
                f_next = dp[r] - P[r+1]
                # maintain deque monotonic by f[]
                while deq and (dp[deq[-1]-1] - P[deq[-1]]) >= f_next:
                    deq.pop()
                deq.append(r+1)

        return dp[n] if dp[n] < INF else -1
