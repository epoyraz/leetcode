class Solution:
    def numMovesStones(self, a, b, c):
        x, y, z = sorted((a, b, c))
        # Minimum moves
        if y - x == 1 and z - y == 1:
            mn = 0
        elif y - x <= 2 or z - y <= 2:
            mn = 1
        else:
            mn = 2
        # Maximum moves
        mx = (y - x - 1) + (z - y - 1)
        return [mn, mx]
