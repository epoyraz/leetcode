class Solution:
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        # The main idea is to alternate "AA" and "BB" strings without forming "AAA" or "BBB"
        # The maximum number of such alternations is min(x, y)
        # We can use one extra AA or BB (if any left) as long as it doesn't create triple
        pairs = min(x, y)
        extra = 1 if x != y else 0
        return (pairs * 2 + extra + z) * 2
