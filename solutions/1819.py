class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L = 2*n - 1
        res = [0]*L
        # used[i] = True means we still need to place the number i
        used = [False, True] + [True]*(n-1)  # indices 0..n, but we only use 1..n
        
        def dfs(pos):
            # If we've filled every position, we're done
            if pos == L:
                return True
            # Skip already filled slots
            if res[pos] != 0:
                return dfs(pos+1)
            # Try to place the largest possible number at pos
            # First try i=n..2 (needs a pair), then i=1 (single)
            for i in range(n, 1, -1):
                j = pos + i
                if used[i] and j < L and res[j] == 0:
                    # place both occurrences of i
                    used[i] = False
                    res[pos] = res[j] = i
                    if dfs(pos+1):
                        return True
                    # backtrack
                    used[i] = True
                    res[pos] = res[j] = 0
            # Finally, try placing the single 1 if still unused
            if used[1]:
                used[1] = False
                res[pos] = 1
                if dfs(pos+1):
                    return True
                used[1] = True
                res[pos] = 0
            # No valid placement leads to a solution
            return False
        
        dfs(0)
        return res
