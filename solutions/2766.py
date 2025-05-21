class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        # Track seen elements in A and B
        seenA = [False] * (n + 1)
        seenB = [False] * (n + 1)
        common = 0
        result = [0] * n

        for i in range(n):
            a = A[i]
            b = B[i]
            # Mark A[i]
            seenA[a] = True
            if seenB[a]:  # A[i] already appeared in B prefix
                common += 1
            # Mark B[i]
            seenB[b] = True
            if seenA[b]:  # B[i] already appeared in A prefix
                common += 1
            # If a == b, we counted only once because seenB[a] was false before
            result[i] = common

        return result
