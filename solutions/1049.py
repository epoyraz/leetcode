class Solution:
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            rotations_top = rotations_bottom = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float('inf')
                if t != x:
                    rotations_top += 1
                if b != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        candidates = {tops[0], bottoms[0]}
        res = min(check(x) for x in candidates)
        return res if res != float('inf') else -1
