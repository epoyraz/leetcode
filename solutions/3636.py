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
        A = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                A[i][j] = 1

        def mat_mult(X, Y):
            Z = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if X[i][k]:
                        for j in range(26):
                            Z[i][j] = (Z[i][j] + X[i][k] * Y[k][j]) % mod
            return Z

        def mat_pow(mat, power):
            res = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power % 2:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return res

        if t == 0:
            return len(s) % mod

        At = mat_pow(A, t)
        f = [sum(At[c]) % mod for c in range(26)]

        return sum(f[ord(ch) - ord('a')] for ch in s) % mod

    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        even_sum = sum(int(num[i]) for i in range(0, len(num), 2))
        odd_sum = sum(int(num[i]) for i in range(1, len(num), 2))
        return even_sum == odd_sum