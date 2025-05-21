class Solution(object):
    def findLucky(self, arr):
        from collections import Counter
        freq = Counter(arr)
        result = -1
        for num, count in freq.items():
            if num == count:
                result = max(result, num)
        return result
