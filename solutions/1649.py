class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = set([0])
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum - target in seen:
                count += 1
                seen = set([0])
                curr_sum = 0
            else:
                seen.add(curr_sum)

        return count
