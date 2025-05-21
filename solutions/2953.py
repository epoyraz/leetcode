class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        freq = defaultdict(int)
        ans = 0

        # Precompute all (dx, dy) with dx + dy == k
        deltas = [(dx, k - dx) for dx in range(k + 1)]

        for x, y in coordinates:
            # For each possible delta, look up matching previous points
            for dx, dy in deltas:
                xx = x ^ dx
                yy = y ^ dy
                ans += freq[(xx, yy)]
            # Now include current point in freq
            freq[(x, y)] += 1

        return ans
