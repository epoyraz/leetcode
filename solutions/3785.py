class Solution(object):
    def countArrays(self, original, bounds):
        """
        :type original: List[int]
        :type bounds: List[List[int]]
        :rtype: int
        """
        n = len(original)
        base = original[0]
        # Initial lower/upper bounds on copy[0] from i = 0
        lb, ub = bounds[0][0], bounds[0][1]

        # Incorporate constraints from each position i
        for i in range(1, n):
            offset = original[i] - base
            ui, vi = bounds[i]
            lb = max(lb, ui - offset)
            ub = min(ub, vi - offset)
            if lb > ub:
                return 0

        # Number of integer choices for copy[0]
        return ub - lb + 1
