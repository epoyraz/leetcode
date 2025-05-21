class Solution:
    def findBestValue(self, arr, target):
        arr.sort()
        left, right = 0, max(arr)
        result = right
        min_diff = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            curr_sum = sum(min(num, mid) for num in arr)
            diff = abs(curr_sum - target)
            
            if diff < min_diff or (diff == min_diff and mid < result):
                min_diff = diff
                result = mid

            if curr_sum < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
