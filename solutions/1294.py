import collections
import bisect

class RangeFreqQuery:
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        # Map each value to the sorted list of its positions
        self.pos = collections.defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        # If value never appears, frequency is 0
        if value not in self.pos:
            return 0
        lst = self.pos[value]
        # Count indices in lst within [left, right]
        lo = bisect.bisect_left(lst, left)
        hi = bisect.bisect_right(lst, right)
        return hi - lo
