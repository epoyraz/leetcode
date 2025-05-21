class Solution:
    def kWeakestRows(self, mat, k):
        # Compute (soldier_count, row_index) for each row
        counts = []
        for i, row in enumerate(mat):
            # Since rows are 1's then 0's, we can use bisect to find first 0
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] == 1:
                    lo = mid + 1
                else:
                    hi = mid
            counts.append((lo, i))  # lo is the number of 1's

        # Sort by soldier count, then by row index
        counts.sort()
        # Extract the first k row indices
        return [idx for _, idx in counts[:k]]
