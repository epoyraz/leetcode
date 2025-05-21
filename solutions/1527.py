class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        color2, color3 = 6, 6  # For row 1

        for _ in range(1, n):
            new_color2 = (color2 * 3 + color3 * 2) % MOD
            new_color3 = (color2 * 2 + color3 * 2) % MOD
            color2, color3 = new_color2, new_color3

        return (color2 + color3) % MOD
