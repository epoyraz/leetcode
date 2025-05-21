class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        max_elem = max(arr)
        win_count = 0
        current = arr[0]

        for i in range(1, len(arr)):
            if current > arr[i]:
                win_count += 1
            else:
                current = arr[i]
                win_count = 1

            if win_count == k or current == max_elem:
                return current

        return current
