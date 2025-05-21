from collections import defaultdict

class Solution:
    def gridIllumination(self, n, lamps, queries):
        lamp_set = set()
        row = defaultdict(int)
        col = defaultdict(int)
        diag = defaultdict(int)
        anti_diag = defaultdict(int)

        for r, c in lamps:
            if (r, c) in lamp_set:
                continue
            lamp_set.add((r, c))
            row[r] += 1
            col[c] += 1
            diag[r - c] += 1
            anti_diag[r + c] += 1

        ans = []
        for r, c in queries:
            if row[r] > 0 or col[c] > 0 or diag[r - c] > 0 or anti_diag[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)

            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nr, nc = r + dx, c + dy
                    if (nr, nc) in lamp_set:
                        lamp_set.remove((nr, nc))
                        row[nr] -= 1
                        col[nc] -= 1
                        diag[nr - nc] -= 1
                        anti_diag[nr + nc] -= 1

        return ans
