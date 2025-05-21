class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Extract digits
        digits = [int(d) for d in str(n)]
        # Sort descending
        digits.sort(reverse=True)
        # The maximum product is the product of the two largest digits
        return digits[0] * digits[1]
