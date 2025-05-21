class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        pattern_count = defaultdict(int)

        for row in matrix:
            # Normalize by making first element 0 (flip whole row if needed)
            normalized = tuple(val ^ row[0] for val in row)
            pattern_count[normalized] += 1

        return max(pattern_count.values())
