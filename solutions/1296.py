class TreeAncestor(object):
    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        LOG = 16  # since 2^16 > 5e4
        self.LOG = LOG
        self.up = [[-1] * LOG for _ in range(n)]

        for i in range(n):
            self.up[i][0] = parent[i]

        for j in range(1, LOG):
            for i in range(n):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        for j in range(self.LOG):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node
