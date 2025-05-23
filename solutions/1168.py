class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None (modifies arr in-place)
        """
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1
        j = n + zeros - 1  # virtual extended array index

        while i < j:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1
