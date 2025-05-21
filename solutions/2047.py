class Solution:
    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            # Find the row index of the max element in the middle column
            max_row = 0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Compare with left and right neighbors
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < n else -1
            curr_val = mat[max_row][mid]

            if curr_val > left_val and curr_val > right_val:
                return [max_row, mid]
            elif left_val > curr_val:
                right = mid - 1
            else:
                left = mid + 1
