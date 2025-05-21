class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        rank = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (rank.get(x, float('inf')), x))
