class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        # build children list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parents[i]
            children[p].append(i)

        self.max_score = 0
        self.count = 0
        
        def dfs(node):
            # returns size of subtree rooted at node
            total = 1
            score = 1
            for c in children[node]:
                sz = dfs(c)
                total += sz
                score *= sz
            # size of the rest of the tree (above)
            rest = n - total
            if rest:
                score *= rest
            # update global
            if score > self.max_score:
                self.max_score = score
                self.count = 1
            elif score == self.max_score:
                self.count += 1
            return total
        
        dfs(0)
        return self.count