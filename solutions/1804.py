class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        n = len(binary)
        # Count total zeros
        z = binary.count('0')
        # If fewer than 2 zeros, no improvement is possible
        if z < 2:
            return binary
        
        # Find first zero
        first_zero = binary.find('0')
        # Compute the single zero's final position
        p = first_zero + z - 1
        
        # Build the result: all '1's up to p, then '0', then all '1's
        return '1' * p + '0' + '1' * (n - p - 1)
