class Solution(object):
    def differenceOfSums(self, n, m):
        total = n * (n + 1) // 2
        count = n // m
        sum_multiples = m * count * (count + 1) // 2
        return total - 2 * sum_multiples
