import sys
sys.setrecursionlimit(10**7)

mod = 10**9 + 7

class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        # Build transition matrix A: A[i][j] = 1 if char i transforms to char j
        A = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                A[i][j] = 1

        # Matrix multiplication mod
        def mat_mult(X, Y):
            Z = [[0] * 26 for _ in range(26)]
            for i in range(26):
                Xi = X[i]
                Zi = Z[i]
                for k in range(26):
                    v = Xi[k]
                    if v:
                        Yk = Y[k]
                        for j in range(26):
                            Zi[j] = (Zi[j] + v * Yk[j]) % mod
            return Z

        # Fast exponentiation of matrix
        def mat_pow(mat, power):
            # identity matrix
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                res[i][i] = 1
            M = mat
            while power > 0:
                if power & 1:
                    res = mat_mult(res, M)
                M = mat_mult(M, M)
                power >>= 1
            return res

        # Base: t=0 => each char contributes len 1
        if t == 0:
            return len(s) % mod

        # Compute A^t
        At = mat_pow(A, t)
        # f_t[c] = total length contribution of starting char c
        f = [sum(At[c][j] for j in range(26)) % mod for c in range(26)]

        # Sum over original string
        ans = 0
        for ch in s:
            ans = (ans + f[ord(ch) - ord('a')]) % mod
        return ans
