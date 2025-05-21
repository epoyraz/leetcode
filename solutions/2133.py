class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        result = 0
        for i in range(len(nums)):
            prefix = nums[i]
            if target.startswith(prefix):
                suffix = target[len(prefix):]
                if suffix in count:
                    result += count[suffix]
                    if prefix == suffix:
                        result -= 1  # Exclude the i == j case
        return result
