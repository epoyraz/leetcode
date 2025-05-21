class Solution(object):
    def countCells(self, grid, pattern):
        """
        :type grid: List[List[str]]
        :type pattern: str
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        N = m * n
        L = len(pattern)
        
        # 1. Build H and V strings
        H = [''] * N
        V = [''] * N
        for r in range(m):
            for c in range(n):
                idxH = r * n + c
                idxV = c * m + r
                H[idxH] = grid[r][c]
                V[idxV] = grid[r][c]
        H = ''.join(H)
        V = ''.join(V)
        
        # 2. Build KMP LPS array for pattern
        lps = [0] * L
        j = 0
        for i in range(1, L):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        
        # Helper to mark coverage in diff array
        def mark_matches(text, diff):
            j = 0
            for i, ch in enumerate(text):
                while j > 0 and ch != pattern[j]:
                    j = lps[j-1]
                if ch == pattern[j]:
                    j += 1
                    if j == L:
                        start = i - L + 1
                        diff[start] += 1
                        diff[start + L] -= 1
                        j = lps[j-1]
                # otherwise continue
                
        # 3. Diff arrays for H and V
        diffH = [0] * (N + 1)
        diffV = [0] * (N + 1)
        
        mark_matches(H, diffH)
        mark_matches(V, diffV)
        
        # 4. Prefix-sum to get coverage counts
        covH = [0] * N
        covV = [0] * N
        running = 0
        for i in range(N):
            running += diffH[i]
            covH[i] = running
        running = 0
        for i in range(N):
            running += diffV[i]
            covV[i] = running
        
        # 5. Count cells where both covered > 0
        ans = 0
        for r in range(m):
            baseH = r * n
            for c in range(n):
                if covH[baseH + c] > 0 and covV[c * m + r] > 0:
                    ans += 1
        return ans
