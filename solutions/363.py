import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                
                prefix_sums = [0]
                curr_sum = 0
                for sum_ in row_sum:
                    curr_sum += sum_
                    idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                    if idx < len(prefix_sums):
                        res = max(res, curr_sum - prefix_sums[idx])
                    bisect.insort(prefix_sums, curr_sum)
        
        return res
