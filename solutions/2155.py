class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_sum = mean * (n + m)
        current_sum = sum(rolls)
        missing_sum = total_sum - current_sum

        if missing_sum < n or missing_sum > 6 * n:
            return []

        # Distribute the missing sum as evenly as possible
        base = missing_sum // n
        extra = missing_sum % n

        result = [base] * n
        for i in range(extra):
            result[i] += 1

        return result
