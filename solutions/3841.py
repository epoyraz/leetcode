class Solution(object):
    def concatenatedDivisibility(self, nums, k):
        n = len(nums)
        fullMask = (1 << n) - 1

        # 1) Precompute lengths, mods, total digits, and powers of ten mod k
        lens = [len(str(x)) for x in nums]
        modv = [x % k for x in nums]
        total_digits = sum(lens)

        p10 = [1] * (total_digits + 1)
        for i in range(1, total_digits + 1):
            p10[i] = (p10[i-1] * 10) % k

        # 2) Build dp[mask][r]: can unused=mask be arranged to remainder=r?
        dp = [[False] * k for _ in range(1 << n)]
        dp[0][0] = True

        masks_by_pc = [[] for _ in range(n+1)]
        for mask in range(1 << n):
            masks_by_pc[bin(mask).count('1')].append(mask)

        for pc in range(1, n+1):
            for mask in masks_by_pc[pc]:
                arr_dp = dp[mask]
                m = mask
                while m:
                    low = m & -m
                    i = low.bit_length() - 1
                    m ^= low
                    prevMask = mask ^ (1 << i)
                    L = lens[i]
                    mul = p10[L]
                    mv = modv[i]
                    for prev in range(k):
                        if dp[prevMask][prev]:
                            arr_dp[(prev * mul + mv) % k] = True
                    if all(arr_dp):
                        break

        if not dp[fullMask][0]:
            return []

        # 3) Forward reconstruct the lexicographically smallest valid perm
        res = []
        mask = fullMask
        rem_pref = 0
        used_digits = 0

        for _ in range(n):
            found = False
            for i in sorted(range(n), key=lambda i: nums[i]):
                if not (mask & (1 << i)):
                    continue
                # simulate picking nums[i] next
                # 3a) update prefix remainder and digits
                L = lens[i]
                P_new = (rem_pref * p10[L] + modv[i]) % k
                d_new = used_digits + L
                # 3b) compute what remainder the suffix must have
                suffix_len = total_digits - d_new
                target = (-P_new * p10[suffix_len]) % k

                rem_mask = mask ^ (1 << i)
                if dp[rem_mask][target]:
                    # pick i
                    res.append(nums[i])
                    rem_pref = P_new
                    used_digits = d_new
                    mask = rem_mask
                    found = True
                    break
            if not found:
                return []   # should not happen if dp[fullMask][0]

        return res
