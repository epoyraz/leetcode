class Solution(object):
    def maxRemovals(self, source, pattern, targetIndices):
        n, m = len(source), len(pattern)
        # Step 1: weight[i] = 1 if i in targetIndices else 0
        T = set(targetIndices)
        weight = [1 if i in T else 0 for i in range(n)]
        
        # dp[j] = minimum total weight to match pattern[:j]
        # using a subsequence of source scanned so far.
        INF = 10**9
        dp = [INF] * (m + 1)
        dp[0] = 0
        
        # Step 2: Build dp over the source string
        for i, ch in enumerate(source):
            w = weight[i]
            # go backwards to avoid overwriting dp[j] before using it
            for j in range(m - 1, -1, -1):
                if pattern[j] == ch:
                    # we can extend a match of length j to length j+1
                    cand = dp[j] + w
                    if cand < dp[j + 1]:
                        dp[j + 1] = cand
        
        # dp[m] is the minimum number of targetIndices positions
        # we were forced to âuseâ in matching the entire pattern.
        min_conflicts = dp[m]
        
        # Step 3: We can remove all the other targetIndices
        return len(targetIndices) - min_conflicts
