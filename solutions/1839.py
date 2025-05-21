class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        for i in range(n - 1):
            arr[i + 1] = arr[i] ^ encoded[i]
        return arr
