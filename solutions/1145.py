class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        from collections import defaultdict
        
        m, n = len(matrix), len(matrix[0])
        result = 0

        # Precompute prefix sums for each row
        for row in matrix:
            for c in range(1, n):
                row[c] += row[c - 1]

        # Fix column range [c1, c2]
        for c1 in range(n):
            for c2 in range(c1, n):
                counter = defaultdict(int)
                counter[0] = 1  # Base case
                curr_sum = 0

                for r in range(m):
                    # Get sum of elements from column c1 to c2 in row r
                    row_sum = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    curr_sum += row_sum
                    result += counter[curr_sum - target]
                    counter[curr_sum] += 1

        return result
