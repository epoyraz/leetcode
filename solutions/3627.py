import sys
sys.setrecursionlimit(10**7)

mod = 10**9 + 7

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        import heapq
        n = len(moveTime)
        m = len(moveTime[0])
        # dist[r][c]: min time to arrive at room (r,c)
        INF = 10**30
        dist = [[INF] * m for _ in range(n)]
        # start at (0,0) at time 0
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (time, r, c)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while pq:
            t, r, c = heapq.heappop(pq)
            if t > dist[r][c]:
                continue
            # reached target
            if r == n-1 and c == m-1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    # can depart at time >= open time of neighbor
                    depart = max(t, moveTime[nr][nc])
                    arrive = depart + 1
                    if arrive < dist[nr][nc]:
                        dist[nr][nc] = arrive
                        heapq.heappush(pq, (arrive, nr, nc))
        # unreachable
        return -1

# existing methods below remain unchanged
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        A = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                A[i][j] = 1

        def mat_mult(X, Y):
            Z = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if X[i][k]:
                        for j in range(26):
                            Z[i][j] = (Z[i][j] + X[i][k] * Y[k][j]) % mod
            return Z

        def mat_pow(mat, power):
            res = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power % 2:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return res

        if t == 0:
            return len(s) % mod

        At = mat_pow(A, t)
        f = [sum(At[c]) % mod for c in range(26)]

        return sum(f[ord(ch) - ord('a')] for ch in s) % mod

    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even_sum = sum(int(num[i]) for i in range(0, len(num), 2))
        odd_sum = sum(int(num[i]) for i in range(1, len(num), 2))
        return even_sum == odd_sum
