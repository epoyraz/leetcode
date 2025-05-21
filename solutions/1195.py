class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        i = 0
        give = 1

        while candies > 0:
            res[i % num_people] += min(give, candies)
            candies -= give
            give += 1
            i += 1

        return res
