class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        n = len(nums)

        # Slide a window of size k over nums and count appearances of each number in each subarray
        for i in range(n - k + 1):
            window = nums[i:i + k]
            unique = set(window)
            for num in unique:
                count[num] += 1

        # Find all numbers that appear in exactly one subarray and return the largest one
        candidates = [num for num, c in count.items() if c == 1]
        return max(candidates) if candidates else -1
