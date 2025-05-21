class Solution(object):
    def minImpossibleOR(self, nums):
        # Track which singleâbit values appear
        seen = [False]*32
        for v in nums:
            # check if v is a power of two
            if v & (v-1) == 0:
                b = v.bit_length() - 1  # v == 1<<b
                seen[b] = True
        # find the smallest i>=0 such that 2^i wasn't seen
        for i in range(32):
            if not seen[i]:
                return 1 << i
        # (in practice you'll always return before reaching here)
        return 1 << 32
