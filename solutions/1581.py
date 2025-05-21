class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]

        # Sort by custom strength comparator
        arr.sort(key=lambda x: (abs(x - m), x), reverse=True)

        return arr[:k]
