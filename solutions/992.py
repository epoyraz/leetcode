class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        kept = []
        res = 0

        for col in range(m):
            # Check if adding this column keeps rows sorted
            if all(
                tuple(strs[i][k] for k in kept + [col]) >=
                tuple(strs[i - 1][k] for k in kept + [col])
                for i in range(1, n)
            ):
                kept.append(col)
            else:
                res += 1

        return res
