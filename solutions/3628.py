import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n = len(moveTime)
        m = len(moveTime[0])
        INF = 10**30
        # dist[r][c][p]: minimum time to reach (r,c) with next-move parity p
        # p = 0 => next move takes 1 second; p = 1 => next move takes 2 seconds
        dist = [[[INF, INF] for _ in range(m)] for __ in range(n)]
        dist[0][0][0] = 0
        # heap entries: (current_time, r, c, parity)
        pq = [(0, 0, 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while pq:
            t, r, c, p = heapq.heappop(pq)
            if t > dist[r][c][p]:
                continue
            # if we've reached the target, return immediately
            if r == n-1 and c == m-1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    # must wait until room (nr,nc) is open
                    depart = max(t, moveTime[nr][nc])
                    # move duration alternates: 1s if p==0, else 2s
                    duration = 1 if p == 0 else 2
                    arrive = depart + duration
                    np = 1 - p
                    if arrive < dist[nr][nc][np]:
                        dist[nr][nc][np] = arrive
                        heapq.heappush(pq, (arrive, nr, nc, np))
        # if unreachable
        return -1
