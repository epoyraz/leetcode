class Solution(object):
    def minimumOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        prev = 0  # think of diff[-1] = 0
        for i in range(n):
            cur = target[i] - nums[i]
            total += abs(cur - prev)
            prev = cur
        # account for returning to diff[n] = 0
        total += abs(prev - 0)
        # each operation changes two "jumps" by 1, so divide by 2
        return total // 2
