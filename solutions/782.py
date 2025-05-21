class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
