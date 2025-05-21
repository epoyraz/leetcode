class Solution(object):
    def countMatchingSubarrays(self, nums, pattern):
        """
        :type nums: List[int]
        :type pattern: List[int]
        :rtype: int
        """
        n, m = len(nums), len(pattern)
        count = 0
        for i in range(n - m):
            match = True
            for k, p in enumerate(pattern):
                if p == 1 and not (nums[i + k + 1] > nums[i + k]):
                    match = False
                    break
                if p == 0 and not (nums[i + k + 1] == nums[i + k]):
                    match = False
                    break
                if p == -1 and not (nums[i + k + 1] < nums[i + k]):
                    match = False
                    break
            if match:
                count += 1
        return count
