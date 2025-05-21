class Solution(object):
    def minOrAfterOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # final number of segments after exactly k merges
        need = n - k  
        # initial OR of all numbers
        cur_or = 0
        for v in nums:
            cur_or |= v

        MAXB = 30
        forbidden = 0  # bits we have successfully cleared

        # try clearing bits from high to low
        for b in range(MAXB - 1, -1, -1):
            bit = 1 << b
            # only consider if this bit is currently set
            if not (cur_or & bit):
                continue

            # candidate forbidden bits if we clear this one
            cand = forbidden | bit

            # greedy scan: count how many segments we can form
            # such that each segment's AND has zeros in all bits in 'cand'
            segments = 0
            mask = cand
            curr_zeros = 0
            for v in nums:
                # mark zeros for this element in the forbidden bits
                curr_zeros |= ((~v) & mask)
                # once we've seen zeros for every forbidden bit, cut a segment
                if curr_zeros == mask:
                    segments += 1
                    curr_zeros = 0

            # if we can get at least 'need' segments, it's feasible
            if segments >= need:
                # accept clearing this bit
                forbidden = cand
                cur_or ^= bit

        return cur_or
