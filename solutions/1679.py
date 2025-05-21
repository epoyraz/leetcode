class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        # find longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left+1]:
            left += 1
        if left == n - 1:
            return 0
        # find longest non-decreasing suffix
        right = n - 1
        while right - 1 >= 0 and arr[right-1] <= arr[right]:
            right -= 1
        # remove suffix or prefix entirely
        ans = min(n - 1 - left, right)
        # try merging prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans
