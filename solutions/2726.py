import bisect
from collections import deque

class Solution:
    def minReverseOperations(self, n, p, banned, k):
        # Initialize
        banned_set = set(banned)
        dist = [-1] * n
        dist[p] = 0
        # Prepare available targets by parity, excluding start and banned
        available = [[], []]
        for i in range(n):
            if i != p and i not in banned_set:
                available[i & 1].append(i)
        for arr in available:
            arr.sort()

        q = deque([p])
        # BFS
        while q:
            u = q.popleft()
            # Compute valid start range s in [u-k+1, u] â© [0, n-k]
            s_min = max(0, u - k + 1)
            s_max = min(u, n - k)
            if s_min > s_max:
                continue
            # Map s to new positions v = 2*s + k - 1 - u
            new_low = 2 * s_min + k - 1 - u
            new_high = 2 * s_max + k - 1 - u
            mod = new_low & 1
            arr = available[mod]
            # Collect all v in [new_low, new_high]
            l = bisect.bisect_left(arr, new_low)
            i = l
            while i < len(arr) and arr[i] <= new_high:
                v = arr[i]
                dist[v] = dist[u] + 1
                q.append(v)
                i += 1
            # Remove visited slice
            del arr[l:i]

        return dist