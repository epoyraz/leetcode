class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        mismatch_start_with_0 = 0
        mismatch_start_with_1 = 0

        for i, ch in enumerate(s):
            expected_0 = str(i % 2)         # Pattern: 0, 1, 0, 1,...
            expected_1 = str((i + 1) % 2)   # Pattern: 1, 0, 1, 0,...
            
            if ch != expected_0:
                mismatch_start_with_0 += 1
            if ch != expected_1:
                mismatch_start_with_1 += 1

        return min(mismatch_start_with_0, mismatch_start_with_1)
