class Solution:
    def maximumProduct(self, nums, k):
        MOD = 10**9 + 7

        # 1) Sort and append a big sentinel
        A = sorted(nums)
        A.append(10**18)

        n = len(nums)
        i = 0
        base = A[0]

        # 2) Level up the smallest (i+1) items in batches
        while True:
            diff = A[i+1] - base
            needed = diff * (i+1)

            if needed <= k:
                # we can raise all of the first i+1 items up to A[i+1]
                k -= needed
                base = A[i+1]
                i += 1
            else:
                # can't fully reach next levelâdistribute the rest of k over the first i+1 items
                q, r = divmod(k, i+1)

                # 3) Compute the final product
                prod = 1

                # r of them get base + q + 1
                prod = prod * pow(base + q + 1, r, MOD) % MOD
                # (i+1 - r) of them get base + q
                prod = prod * pow(base + q, (i+1 - r), MOD) % MOD

                # the remaining items (from i+1 up to n-1) stay at their original values
                for j in range(i+1, n):
                    prod = (prod * (A[j] % MOD)) % MOD

                return prod
