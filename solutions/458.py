import math

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        tests = minutesToTest // minutesToDie
        pigs = 0
        while (tests + 1) ** pigs < buckets:
            pigs += 1
        return pigs
