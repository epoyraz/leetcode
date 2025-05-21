class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        d, v = indexDifference, valueDifference

        # Edge case: any pair works if both diffs are zero
        if d == 0 and v == 0:
            return [0, 0]

        # Build prefix max/min with their indices
        pref_max = [0] * n
        pref_min = [0] * n
        pref_max_idx = [0] * n
        pref_min_idx = [0] * n

        curr_max = nums[0]
        curr_min = nums[0]
        imax = imin = 0
        pref_max[0], pref_min[0] = curr_max, curr_min
        pref_max_idx[0], pref_min_idx[0] = 0, 0
        for i in range(1, n):
            if nums[i] > curr_max:
                curr_max, imax = nums[i], i
            if nums[i] < curr_min:
                curr_min, imin = nums[i], i
            pref_max[i], pref_max_idx[i] = curr_max, imax
            pref_min[i], pref_min_idx[i] = curr_min, imin

        # Build suffix max/min with their indices
        suff_max = [0] * n
        suff_min = [0] * n
        suff_max_idx = [0] * n
        suff_min_idx = [0] * n

        curr_max = nums[-1]
        curr_min = nums[-1]
        imax = imin = n - 1
        suff_max[-1], suff_min[-1] = curr_max, curr_min
        suff_max_idx[-1], suff_min_idx[-1] = imax, imin
        for i in range(n - 2, -1, -1):
            if nums[i] > curr_max:
                curr_max, imax = nums[i], i
            if nums[i] < curr_min:
                curr_min, imin = nums[i], i
            suff_max[i], suff_max_idx[i] = curr_max, imax
            suff_min[i], suff_min_idx[i] = curr_min, imin

        # For each i, check prefix [0..i-d] and suffix [i+d..n-1]
        for i in range(n):
            # prefix side
            j = i - d
            if j >= 0:
                # check against prefix max
                if abs(nums[i] - pref_max[j]) >= v:
                    return [i, pref_max_idx[j]]
                # check against prefix min
                if abs(nums[i] - pref_min[j]) >= v:
                    return [i, pref_min_idx[j]]
            # suffix side
            j = i + d
            if j < n:
                if abs(suff_max[j] - nums[i]) >= v:
                    return [i, suff_max_idx[j]]
                if abs(suff_min[j] - nums[i]) >= v:
                    return [i, suff_min_idx[j]]

        return [-1, -1]
