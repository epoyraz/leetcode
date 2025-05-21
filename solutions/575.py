class Solution(object):
    def distributeCandies(self, candyType):
        # You can eat at most n/2 candies, and you want as many distinct types as possible.
        # The maximum distinct types you can eat is the minimum of:
        #   - the number of unique candy types
        #   - n/2 (the total candies you are allowed to eat)
        return min(len(set(candyType)), len(candyType) // 2)
