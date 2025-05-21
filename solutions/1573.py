class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')
        
        # min_len[i]: min length of subarray that ends at or before i with sum == target
        min_len = [INF] * n
        
        left = 0
        total = 0
        best = INF
        res = INF
        
        for right in range(n):
            total += arr[right]
            
            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                curr_len = right - left + 1
                if left > 0 and min_len[left - 1] != INF:
                    res = min(res, curr_len + min_len[left - 1])
                best = min(best, curr_len)

            min_len[right] = best

        return res if res != INF else -1
