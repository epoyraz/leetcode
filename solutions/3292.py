class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        n, m = len(nums), len(changeIndices)
        # convert to 0-based
        change = [c-1 for c in changeIndices]
        
        # check if by time t we can finish
        def can(t):
            # find for each index i its last marking time â¤ t
            last = [-1]*n
            for s in range(t):
                last[change[s]] = s+1   # store 1-based time
            # every index must appear
            for i in range(n):
                if last[i] < 0:
                    return False
            
            # build (deadline, work) pairs
            tasks = [(last[i]-1, nums[i]) for i in range(n)]
            tasks.sort(key=lambda x: x[0])  # sort by deadline
            
            # prefix sums of work
            prefix = [0]*(n+1)
            for i, (_, w) in enumerate(tasks):
                prefix[i+1] = prefix[i] + w
            
            # EDFâstyle check: for each distinct deadline D, let
            #   k_prev = # tasks with deadline < D,
            #   total_work = sum of all tasks with deadline â¤ D,
            # and ensure total_work â¤ (D â k_prev) free slots.
            i = 0
            while i < n:
                D = tasks[i][0]
                # find block of tasks with same deadline
                j = i+1
                while j < n and tasks[j][0] == D:
                    j += 1
                k_prev = i
                # worstâcase total_work is prefix[j]
                if prefix[j] > D - k_prev:
                    return False
                i = j
            
            return True
        
        # binary search earliest t in [1..m]
        ans = m+1
        lo, hi = 1, m
        while lo <= hi:
            mid = (lo+hi)//2
            if can(mid):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        
        return ans if ans <= m else -1
