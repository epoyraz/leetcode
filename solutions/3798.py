import sys
sys.setrecursionlimit(10**7)
import collections

class Solution(object):
    def longestSpecialPath(self, edges, nums):
        n = len(nums)
        # build adjacency and then children list rooted at 0
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        children = [[] for _ in range(n)]
        q = collections.deque([0])
        parent = [-1]*n
        parent[0] = 0
        while q:
            u = q.popleft()
            for v,w in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    children[u].append((v,w))
                    q.append(v)

        # sliding-window state
        maxval = max(nums) if nums else 0
        self.counts = [0]*(maxval+1)
        self.dup2 = 0
        self.dup3plus = 0
        self.ops = []        # stack of ("inc"/"dec", val)
        self.path = []       # node indices
        self.dists = []      # cumulative distances
        self.L = 0           # left index of valid window
        self.bestLen = 0
        self.bestNodes = 1

        # define dfs as method
        def dfs(u, curDist):
            # snapshot
            snap_ops = len(self.ops)
            snap_L   = self.L

            # push u
            self.path.append(u)
            self.dists.append(curDist)
            val = nums[u]
            # inc count
            self.counts[val] += 1
            if self.counts[val] == 2:
                self.dup2 += 1
            elif self.counts[val] == 3:
                self.dup2 -= 1
                self.dup3plus += 1
            self.ops.append(("inc", val))

            # shrink from left until valid
            while self.dup2 > 1 or self.dup3plus > 0:
                wnode = self.path[self.L]
                wval = nums[wnode]
                # dec count
                self.counts[wval] -= 1
                if self.counts[wval] == 1:
                    self.dup2 -= 1
                elif self.counts[wval] == 2:
                    self.dup3plus -= 1
                    self.dup2 += 1
                self.ops.append(("dec", wval))
                self.L += 1

            # update best
            windowLen = curDist - self.dists[self.L]
            windowNodes = len(self.path) - self.L
            if windowLen > self.bestLen:
                self.bestLen = windowLen
                self.bestNodes = windowNodes
            elif windowLen == self.bestLen and windowNodes < self.bestNodes:
                self.bestNodes = windowNodes

            # recurse
            for v,w in children[u]:
                dfs(v, curDist + w)

            # undo
            while len(self.ops) > snap_ops:
                typ, v = self.ops.pop()
                if typ == "inc":
                    # we had done counts[v] += 1
                    self.counts[v] -= 1
                    if self.counts[v] == 1:
                        self.dup2 -= 1
                    elif self.counts[v] == 2:
                        self.dup3plus -= 1
                        self.dup2 += 1
                else:
                    # we had done counts[v] -= 1
                    self.counts[v] += 1
                    if self.counts[v] == 2:
                        self.dup2 += 1
                    elif self.counts[v] == 3:
                        self.dup2 -= 1
                        self.dup3plus += 1

            # restore L, pop path/dists
            self.L = snap_L
            self.path.pop()
            self.dists.pop()

        # start DFS from root (0) with distance 0
        dfs(0, 0)
        return [self.bestLen, self.bestNodes]
