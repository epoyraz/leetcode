class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter

        count = Counter((x % k + k) % k for x in arr)  # handle negative numbers

        for rem in count:
            if rem == 0:
                if count[rem] % 2 != 0:
                    return False
            elif rem * 2 == k:
                if count[rem] % 2 != 0:
                    return False
            else:
                if count[rem] != count[k - rem]:
                    return False

        return True
