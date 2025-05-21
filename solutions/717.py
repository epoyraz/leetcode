class Solution(object):
    def isOneBitCharacter(self, bits):
        i, n = 0, len(bits)
        # Parse until the last bit
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        # If we land on the last index, it's a one-bit character
        return i == n - 1
