class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0

        for start in range(n):
            if nums[start] != 0:
                continue
            for direction in (-1, 1):
                arr = nums[:]      # copy
                curr = start
                d = direction
                # simulate until we step out of [0..n-1]
                while 0 <= curr < n:
                    if arr[curr] == 0:
                        curr += d
                    else:
                        # decrement, reverse, and step
                        arr[curr] -= 1
                        d = -d
                        curr += d
                # after exiting, check if all zero
                if all(v == 0 for v in arr):
                    res += 1

        return res
