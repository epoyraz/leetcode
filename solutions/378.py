class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        
        def count_less_equal(x):
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count
        
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
