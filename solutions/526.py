class Solution:
    def countArrangement(self, n):
        def backtrack(pos, visited):
            if pos > n:
                return 1
            total = 0
            for i in range(1, n + 1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    total += backtrack(pos + 1, visited)
                    visited[i] = False
            return total

        return backtrack(1, [False] * (n + 1))
