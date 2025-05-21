class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        no_del = [0] * n
        one_del = [0] * n
        
        no_del[0] = arr[0]
        one_del[0] = float('-inf')
        res = arr[0]
        
        for i in range(1, n):
            no_del[i] = max(arr[i], no_del[i-1] + arr[i])
            one_del[i] = max(one_del[i-1] + arr[i], no_del[i-1])  # delete current or one before
            res = max(res, no_del[i], one_del[i])
        
        return res
