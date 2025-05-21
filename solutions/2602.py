class Solution:
    def captureForts(self, forts):
        max_captured = 0
        n = len(forts)
        prev = -1

        for i in range(n):
            if forts[i] != 0:
                if prev != -1 and forts[i] != forts[prev]:
                    max_captured = max(max_captured, i - prev - 1)
                prev = i

        return max_captured
