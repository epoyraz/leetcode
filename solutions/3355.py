class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        n = len(possible)
        # Convert to +1 (clear) / -1 (fail)
        arr = [1 if x == 1 else -1 for x in possible]
        
        S = sum(arr)
        prefix = 0
        
        # Alice must take at least 1 and Bob at least 1,
        # so k ranges from 1 to n-1.
        for k in range(1, n):
            prefix += arr[k-1]
            # check 2 * AliceScore > total S
            if 2 * prefix > S:
                return k
        
        return -1
