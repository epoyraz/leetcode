class Solution(object):
    def maxValue(self, n, index, maxSum):
        def calc_sum(peak, length):
            if peak > length:
                total = (peak + peak - length + 1) * length // 2
            else:
                total = (peak + 1) * peak // 2 + (length - peak)
            return total

        def is_valid(peak):
            left = calc_sum(peak - 1, index)
            right = calc_sum(peak - 1, n - index - 1)
            return left + right + peak <= maxSum

        low, high = 1, maxSum
        while low < high:
            mid = (low + high + 1) // 2
            if is_valid(mid):
                low = mid
            else:
                high = mid - 1
        return low
