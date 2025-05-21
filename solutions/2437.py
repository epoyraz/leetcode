class Solution(object):
    def maximumGroups(self, grades):
        n = len(grades)
        k = 0
        while (k + 1) * (k + 2) // 2 <= n:
            k += 1
        return k
