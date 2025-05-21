class Solution:
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        k = k % n  # Only k mod n matters, since it's cyclic

        def shift_row(row, direction):
            if direction == 'left':
                return row[k:] + row[:k]
            else:
                return row[-k:] + row[:-k]

        for i in range(m):
            if i % 2 == 0:
                shifted = shift_row(mat[i], 'left')
            else:
                shifted = shift_row(mat[i], 'right')
            if shifted != mat[i]:
                return False
        return True
