class Solution:
    def trimMean(self, arr):
        arr.sort()
        n = len(arr)
        cut = n // 20                # 5% of n, and n is a multiple of 20
        middle_sum = sum(arr[cut: n - cut])
        # force floatingâpoint division
        return middle_sum * 1.0 / (n - 2 * cut)
