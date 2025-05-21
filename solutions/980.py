class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        # Precompute overlap lengths: overlap[i][j] = max k where
        # suffix of words[i] of length k == prefix of words[j] of length k
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # find max overlap
                w1, w2 = words[i], words[j]
                max_ol = min(len(w1), len(w2))
                # check k from max down to 1
                for k in range(max_ol, 0, -1):
                    if w1.endswith(w2[:k]):
                        overlap[i][j] = k
                        break

        # DP[mask][i]: length of shortest superstring for set mask ending with word i
        N = 1 << n
        dp = [[float('inf')]*n for _ in range(N)]
        parent = [[-1]*n for _ in range(N)]
        # Initialize with single words
        for i in range(n):
            dp[1<<i][i] = len(words[i])

        # Fill DP
        for mask in range(N):
            for last in range(n):
                if not (mask & (1<<last)):
                    continue
                prev_mask = mask ^ (1<<last)
                if prev_mask == 0:
                    continue
                # Try all possible previous words
                for prev in range(n):
                    if not (prev_mask & (1<<prev)):
                        continue
                    val = dp[prev_mask][prev] + len(words[last]) - overlap[prev][last]
                    if val < dp[mask][last]:
                        dp[mask][last] = val
                        parent[mask][last] = prev

        # Find best end word
        full_mask = N - 1
        min_len = float('inf')
        end = 0
        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                end = i

        # Reconstruct path
        path = []
        mask = full_mask
        while end != -1:
            path.append(end)
            prev = parent[mask][end]
            mask ^= (1 << end)
            end = prev
        path.reverse()

        # Build answer string
        ans = words[path[0]]
        for i in range(1, len(path)):
            i_prev, i_cur = path[i-1], path[i]
            ol = overlap[i_prev][i_cur]
            ans += words[i_cur][ol:]

        return ans
