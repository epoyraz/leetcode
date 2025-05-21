import bisect

class Solution:
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        # 1) Separate alreadyâfull gardens from the rest
        flowers.sort()
        n = len(flowers)
        # number of gardens already >= target
        full0 = bisect.bisect_left(flowers, target)
        full0 = n - full0
        # B = flowers < target
        B = flowers[:n - full0]
        M = len(B)
        
        # 2) Prefix sums on B for raising the minimum
        ps = [0] * (M + 1)
        for i in range(M):
            ps[i+1] = ps[i] + B[i]
        
        # 3) Suffix sums on B for completing gardens
        #    suf[i] = sum of B[i..M-1]
        suf = [0] * (M + 1)
        for i in range(M - 1, -1, -1):
            suf[i] = suf[i+1] + B[i]
        
        best = 0
        
        # 4) Try making f_add of the incomplete gardens full
        for f_add in range(M + 1):
            # cost to make the largest f_add of B full:
            #   = f_add*target - sum of those f_add = f_add*target - suf[M-f_add]
            cost_full_add = f_add * target - suf[M - f_add]
            if cost_full_add > newFlowers:
                break
            
            rem = newFlowers - cost_full_add
            total_full = full0 + f_add
            incomplete = M - f_add
            
            # 5a) If no incomplete remain, only full term
            if incomplete == 0:
                best = max(best, total_full * full)
            else:
                # 5b) Binaryâsearch the maximum m â¤ target-1 we can raise all B[0..incomplete-1] to
                lo, hi = B[0], target - 1
                if lo > hi:
                    m = hi
                else:
                    while lo < hi:
                        mid = (lo + hi + 1) // 2
                        # how many are below mid in B[0..incomplete-1]?
                        idx = bisect.bisect_left(B, mid, 0, incomplete)
                        cost = mid * idx - ps[idx]
                        if cost <= rem:
                            lo = mid
                        else:
                            hi = mid - 1
                    m = lo
                
                best = max(best, total_full * full + m * partial)
        
        return best
