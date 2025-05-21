import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def placedCoins(self, edges, cost):
        """
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: List[int]
        """
        n = len(cost)
        # build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # result array
        res = [0] * n
        
        def dfs(u, parent):
            """
            Returns a tuple for subtree rooted at u:
             - size of subtree
             - max3: list of up to 3 largest costs in this subtree (descending)
             - min2: list of up to 2 smallest costs in this subtree (ascending)
            Also fills res[u].
            """
            size = 1
            max3 = [cost[u]]
            min2 = [cost[u]]
            
            # process children
            for v in adj[u]:
                if v == parent:
                    continue
                c_size, c_max3, c_min2 = dfs(v, u)
                size += c_size
                
                # merge topâ3 largest
                merged_max = max3 + c_max3
                merged_max.sort(reverse=True)
                max3 = merged_max[:3]
                
                # merge bottomâ2 smallest
                merged_min = min2 + c_min2
                merged_min.sort()
                min2 = merged_min[:2]
            
            # compute coins for u
            if size < 3:
                # fewer than 3 nodes â always place 1 coin
                res[u] = 1
            else:
                # candidate 1: product of the three largest positives
                best = float("-inf")
                if len(max3) >= 3:
                    best = max(best, max3[0] * max3[1] * max3[2])
                # candidate 2: product of two smallest (possibly negatives) and the largest
                if len(min2) >= 2:
                    best = max(best, min2[0] * min2[1] * max3[0])
                # if negative, place 0
                res[u] = best if best > 0 else 0
            
            return size, max3, min2
        
        # run DFS from root = 0
        dfs(0, -1)
        return res
