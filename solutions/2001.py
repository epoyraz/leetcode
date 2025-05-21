from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        # visited positions
        visited = [False] * n
        visited[0] = True
        
        q = deque([0])
        # furthest right we've enqueued so far
        furthest = 0
        
        while q:
            i = q.popleft()
            # compute the new window [start, end]
            start = i + minJump
            end = min(i + maxJump, n - 1)
            # only consider from furthest+1 up to end
            for j in range(max(start, furthest + 1), end + 1):
                if s[j] == '0' and not visited[j]:
                    if j == n - 1:
                        return True
                    visited[j] = True
                    q.append(j)
            # update how far we've processed
            furthest = max(furthest, end)
        
        # check if we ever reached n-1 (in case start=0)
        return visited[n - 1]
