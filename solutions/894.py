import random

class Solution(object):
    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.N = n
        self.black = set(blacklist)
        self.M = n - len(blacklist)
        
        # Map for blacklisted numbers in [0, M) to valid numbers >= M
        self.mapping = {}
        # Start from the end of the range
        w = n - 1
        
        # For every blacklisted b < M, find a w >= M that's not blacklisted
        for b in blacklist:
            if b < self.M:
                # Move w down until it's not in black set
                while w in self.black:
                    w -= 1
                self.mapping[b] = w
                w -= 1

    def pick(self):
        """
        :rtype: int
        """
        # Pick uniformly from [0, M)
        x = random.randrange(self.M)
        # If x is remapped, return its mapping, else x itself
        return self.mapping.get(x, x)
