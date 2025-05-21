class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        res = float('inf')
        prev = set()

        for num in arr:
            curr = {num}
            for val in prev:
                curr.add(val & num)
            for val in curr:
                res = min(res, abs(val - target))
            prev = curr

        return res
