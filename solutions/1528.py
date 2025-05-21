class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        return [c + extraCandies >= max_candy for c in candies]
