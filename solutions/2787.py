class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        positions = []

        for i in range(n):
            if s[i] == 'L':
                positions.append(nums[i] - d)
            else:
                positions.append(nums[i] + d)

        positions.sort()
        total = 0
        prefix_sum = 0

        for i in range(n):
            total = (total + i * positions[i] - prefix_sum) % MOD
            prefix_sum = (prefix_sum + positions[i]) % MOD

        return total
