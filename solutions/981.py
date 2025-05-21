class Solution:
    def minDeletionSize(self, strs):
        if not strs:
            return 0
        n, m = len(strs), len(strs[0])
        delete_count = 0

        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break

        return delete_count
