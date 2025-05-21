class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        cnt = nums.count(m)
        # If any b>m is not divisible by m, we can generate a new smaller positive
        # then eliminate everything down to one copy of it.
        for b in nums:
            if b > m and b % m != 0:
                return 1
        # Otherwise all are multiples of m; we end up with ceil(cnt/2).
        return (cnt + 1) // 2
