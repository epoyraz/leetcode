class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr)
        for i in [n // 4, n // 2, 3 * n // 4]:
            candidate = arr[i]
            # Use binary search to count frequency
            left = self.left_bound(arr, candidate)
            right = self.right_bound(arr, candidate)
            if right - left > n // 4:
                return candidate

    def left_bound(self, arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def right_bound(self, arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low
