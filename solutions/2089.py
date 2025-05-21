class Solution(object):
    def maxMatrixSum(self, matrix):
        total = 0
        min_abs = float('inf')
        neg_count = 0
        
        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    neg_count += 1
                    
        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
