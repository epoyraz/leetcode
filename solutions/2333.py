import bisect

class Solution:
    def countRectangles(self, rectangles, points):
        # 1) Bucket rectangle lengths by their height h=1..100
        by_h = [[] for _ in range(101)]
        for L, H in rectangles:
            by_h[H].append(L)
        # Sort each bucket once
        for h in range(1, 101):
            by_h[h].sort()
        
        # 2) Group queries (points) by their y_j
        #    so we can answer them exactly when sweep reaches that y
        qs = [[] for _ in range(101)]
        for idx, (x, y) in enumerate(points):
            qs[y].append((x, idx))
        
        # 3) Sweep y from 100 down to 1, maintaining a sorted list L
        L = []          # merged list of all lengths with height >= current y
        res = [0] * len(points)
        
        for y in range(100, 0, -1):
            # Merge in the rectangles of exactly height y
            # (both L and by_h[y] are sorted)
            if by_h[y]:
                # Standard two-pointer merge into a new list
                merged = []
                i = j = 0
                A, B = L, by_h[y]
                na, nb = len(A), len(B)
                while i < na and j < nb:
                    if A[i] <= B[j]:
                        merged.append(A[i]); i += 1
                    else:
                        merged.append(B[j]); j += 1
                if i < na:
                    merged.extend(A[i:])
                if j < nb:
                    merged.extend(B[j:])
                L = merged
            
            # Answer any queries whose y_j == y
            # Count how many lengths in L are >= x via bisect
            for x, qi in qs[y]:
                # first position where length >= x
                pos = bisect.bisect_left(L, x)
                res[qi] = len(L) - pos
        
        return res
