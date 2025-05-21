class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        # 1âs first
        take1 = min(k, numOnes)
        k -= take1
        total = take1  # each 1 contributes +1

        # then 0âs
        take0 = min(k, numZeros)
        k -= take0
        # total += take0 * 0  // no change

        # finally -1âs
        # whatever remains of k must be from neg-ones
        total -= k   # each contributes -1

        return total
