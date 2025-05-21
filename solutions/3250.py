class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # build sorted lists of fence positions including boundaries
        xs = [1] + sorted(hFences) + [m]
        ys = [1] + sorted(vFences) + [n]
        
        # compute all possible interval lengths on x-axis
        x_diffs = set()
        Lx = len(xs)
        for i in range(Lx):
            for j in range(i+1, Lx):
                x_diffs.add(xs[j] - xs[i])
        
        # compute all possible interval lengths on y-axis
        y_diffs = set()
        Ly = len(ys)
        for i in range(Ly):
            for j in range(i+1, Ly):
                y_diffs.add(ys[j] - ys[i])
        
        # find the largest common length
        common = x_diffs & y_diffs
        if not common:
            return -1
        
        L = max(common)
        return (L * L) % MOD
