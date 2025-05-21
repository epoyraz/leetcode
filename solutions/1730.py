class Solution:
    def specialArray(self, nums):
        n = len(nums)
        # Try every possible x from 0 up to n
        for x in range(n + 1):
            # Count how many numbers are >= x
            cnt = 0
            for v in nums:
                if v >= x:
                    cnt += 1
            # If exactly x numbers are >= x, we've found our answer
            if cnt == x:
                return x
        return -1
