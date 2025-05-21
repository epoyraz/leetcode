class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Helper: sum of multiples of k up to n
        def sum_k(k):
            m = n // k
            return k * m * (m + 1) // 2

        # Inclusion-Exclusion over 3,5,7
        sum3 = sum_k(3)
        sum5 = sum_k(5)
        sum7 = sum_k(7)
        sum15 = sum_k(15)
        sum21 = sum_k(21)
        sum35 = sum_k(35)
        sum105 = sum_k(105)

        return (sum3 + sum5 + sum7
                - sum15 - sum21 - sum35
                + sum105)
