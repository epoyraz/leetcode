class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        if n <= 1:
            return 1
        
        # Record first and last occurrence of each value
        first = {}
        last = {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
        
        # Build forbidden intervals [start, end] over cut positions 0..n-2
        intervals = []
        for v in first:
            f = first[v]
            l = last[v]
            if l > f:
                # forbid cuts at positions f through l-1
                intervals.append((f, l-1))
        
        if not intervals:
            # No forbidden cuts at all
            allowed = n - 1
        else:
            # Merge the intervals
            intervals.sort()
            merged = []
            cur_start, cur_end = intervals[0]
            for s, e in intervals[1:]:
                if s <= cur_end + 1:
                    # overlap or contiguous, extend
                    cur_end = max(cur_end, e)
                else:
                    merged.append((cur_start, cur_end))
                    cur_start, cur_end = s, e
            merged.append((cur_start, cur_end))
            
            # Count forbidden positions
            forbidden = 0
            for s, e in merged:
                forbidden += (e - s + 1)
            allowed = (n - 1) - forbidden
        
        # Each allowed cut may be either present or not
        return pow(2, allowed, MOD)
