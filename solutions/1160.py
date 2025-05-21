class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        from collections import Counter

        count = Counter(tiles)
        self.res = 0

        def backtrack(counter):
            for ch in counter:
                if counter[ch] == 0:
                    continue
                self.res += 1
                counter[ch] -= 1
                backtrack(counter)
                counter[ch] += 1

        backtrack(count)
        return self.res
