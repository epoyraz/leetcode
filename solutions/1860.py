class Solution:
    def kthLargestValue(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        # prev[j] will hold the prefix-xor for column j from the previous row
        prev = [0] * n
        vals = []

        for i in range(m):
            curr = [0] * n
            for j in range(n):
                v = matrix[i][j]
                # xor with above
                if i:
                    v ^= prev[j]
                # xor with left
                if j:
                    v ^= curr[j-1]
                # we've xored above and left twice, so xor the overlap back
                if i and j:
                    v ^= prev[j-1]
                curr[j] = v
                vals.append(v)
            prev = curr

        # sort descending and pick the kâth
        vals.sort(reverse=True)
        return vals[k-1]
