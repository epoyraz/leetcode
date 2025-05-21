class Solution:
    def distributeCookies(self, cookies, k):
        n = len(cookies)
        # Sort descending to place big bags first (improves pruning)
        cookies.sort(reverse=True)
        
        # loads[j] = total cookies for child j
        loads = [0]*k
        self.best = sum(cookies)

        def dfs(i):
            # All bags assigned
            if i == n:
                self.best = min(self.best, max(loads))
                return

            bag = cookies[i]
            # Try giving bag i to each child j
            for j in range(k):
                # Prune if this would not improve best
                if loads[j] + bag >= self.best:
                    continue

                # Assign
                loads[j] += bag
                dfs(i+1)
                loads[j] -= bag

                # Symmetry pruning: if this child had 0 before,
                # no need to try other empty children
                if loads[j] == 0:
                    break

        dfs(0)
        return self.best
