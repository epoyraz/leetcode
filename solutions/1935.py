class Solution(object):
    def reinitializePermutation(self, n):
        def h(j):
            if j < n // 2:
                return 2 * j
            else:
                return 2 * (j - n // 2) + 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        visited = [False] * n
        res = 1
        for i in range(n):
            if not visited[i]:
                cnt = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = h(j)
                    cnt += 1
                if cnt > 0:
                    res = res * cnt / gcd(res, cnt)
        return res
