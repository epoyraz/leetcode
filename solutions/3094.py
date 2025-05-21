class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Count the occurrences of each number
        from collections import Counter
        freq = Counter(nums)
        operations = 0
        # For each frequency, determine the minimum rounds using groups of 2 or 3
        for count in freq.values():
            # If any number appears only once, it's impossible to delete it
            if count == 1:
                return -1
            # Greedy grouping: use as many triplets as possible; the formula (count + 2) // 3
            # gives the minimum number of groups of size 2 or 3 to sum to count,
            # provided count > 1.
            operations += (count + 2) // 3
        return operations
