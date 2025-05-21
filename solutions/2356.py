class Solution:
    def largestCombination(self, candidates):
        # Count how many numbers have each bit set
        bit_counts = [0] * 24  # since candidates[i] <= 10^7 < 2^24
        for x in candidates:
            b = 0
            while x:
                if x & 1:
                    bit_counts[b] += 1
                x >>= 1
                b += 1
        # The largest subset whose AND > 0 must all share at least one common '1' bit
        return max(bit_counts)
