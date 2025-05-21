from collections import defaultdict

MOD = 1000000007
def C2(x):
    return x * (x - 1) // 2

class Solution(object):
    def subsequencesWithMiddleMode(self, nums):
        n = len(nums)
        if n < 5:
            return 0

        suff = defaultdict(int)
        for v in nums:
            suff[v] += 1
        suff_sum_c2 = sum(C2(c) for c in suff.values())

        pref = defaultdict(int)
        pref_sum_c2 = 0

        ans = 0

        for k, v in enumerate(nums):
            old = suff[v]
            suff_sum_c2 -= C2(old)
            old -= 1
            if old:
                suff[v] = old
                suff_sum_c2 += C2(old)
            else:
                del suff[v]

            left_len  = k
            right_len = n - k - 1
            if left_len < 2 or right_len < 2:
                pref_sum_c2 -= C2(pref[v])
                pref[v] += 1
                pref_sum_c2 += C2(pref[v])
                continue

            pref_v = pref.get(v, 0)
            suff_v = suff.get(v, 0)

            lenNL = left_len  - pref_v
            lenNR = right_len - suff_v

            L0 = C2(lenNL)
            L1 = pref_v * lenNL
            L2 = C2(pref_v)

            R0 = C2(lenNR)
            R1 = suff_v * lenNR
            R2 = C2(suff_v)

            dupL = (pref_sum_c2 - C2(pref_v))
            dupR = (suff_sum_c2 - C2(suff_v))

            LD = L0 - dupL
            RD = R0 - dupR

            ans += (L0 * R2 + L1 * R1 + L2 * R0)
            ans += (L1 * R2 + L2 * R1)
            ans += (L2 * R2)
            ans %= MOD

            if pref_v and RD:
                S1 = 0
                for x in pref:
                    if x == v or pref[x] == 0:
                        continue
                    suff_x = suff.get(x, 0)
                    S1 += pref[x] * suff_x * (lenNR - suff_x)
                contrib = pref_v * (RD * lenNL - S1)
                ans = (ans + contrib) % MOD

            if suff_v and LD:
                S2 = 0
                for x in suff:
                    if x == v or suff[x] == 0:
                        continue
                    pref_x = pref.get(x, 0)
                    S2 += suff[x] * pref_x * (lenNL - pref_x)
                contrib = suff_v * (LD * lenNR - S2)
                ans = (ans + contrib) % MOD

            pref_sum_c2 -= C2(pref[v])
            pref[v] += 1
            pref_sum_c2 += C2(pref[v])

        return ans % MOD
