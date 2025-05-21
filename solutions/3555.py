class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        Perform k operations: each time find the first minimum element and multiply it.
        """
        # Copy list to avoid mutating input
        arr = list(nums)
        n = len(arr)
        for _ in range(k):
            # Find index of first minimum
            min_val = arr[0]
            min_idx = 0
            for i in range(1, n):
                if arr[i] < min_val:
                    min_val = arr[i]
                    min_idx = i
            # Multiply
            arr[min_idx] = arr[min_idx] * multiplier
        return arr