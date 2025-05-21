class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        N = 1 << n

        # precompute bit counts for masks 0..(2^n - 1)
        bits = [0] * N
        for mask in range(1, N):
            bits[mask] = bits[mask >> 1] + (mask & 1)

        INF = 10**18
        dp = [INF] * N
        dp[0] = 0

        # dp[mask] = min XOR-sum pairing the set bits of mask in nums2
        # with the first bits=popcount(mask) elements of nums1
        for mask in range(N):
            k = bits[mask]  # next index in nums1 to pair
            for j in range(n):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    cost = dp[mask] + (nums1[k] ^ nums2[j])
                    if cost < dp[new_mask]:
                        dp[new_mask] = cost

        return dp[N - 1]
