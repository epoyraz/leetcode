class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0]) if mat else 0
        # if the total number of elements doesn't match, return original
        if m * n != r * c:
            return mat
        # flatten in row-traversing order
        flat = []
        for row in mat:
            for num in row:
                flat.append(num)
        # build the reshaped matrix
        res = []
        for i in range(r):
            res.append(flat[i * c:(i + 1) * c])
        return res
