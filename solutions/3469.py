import math

class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """

        # Helper: floor of sqrt(x)
        def isqrt(x):
            return int(math.sqrt(x))

        # For odd h = 2*k - 1:
        #   odd rows sum = k^2
        #   even rows sum = k*(k-1)
        # Starting with red: require k^2 <= red  and  k*(k-1) <= blue
        k1 = min(
            isqrt(red),
            (1 + int(math.sqrt(1 + 4*blue))) // 2
        )
        h_odd_R = 2*k1 - 1

        # Starting with blue:
        k2 = min(
            isqrt(blue),
            (1 + int(math.sqrt(1 + 4*red))) // 2
        )
        h_odd_B = 2*k2 - 1

        # For even h = 2*k:
        #   odd rows sum = k^2
        #   even rows sum = k*(k+1)
        # Starting with red: require k^2 <= red  and  k*(k+1) <= blue
        k3 = min(
            isqrt(red),
            ( -1 + int(math.sqrt(1 + 4*blue)) ) // 2
        )
        h_even_R = 2*k3

        # Starting with blue:
        k4 = min(
            isqrt(blue),
            ( -1 + int(math.sqrt(1 + 4*red)) ) // 2
        )
        h_even_B = 2*k4

        return max(h_odd_R, h_odd_B, h_even_R, h_even_B)
