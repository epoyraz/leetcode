class Solution:
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        # 1) Enumerate all baseâ3 masks of length n
        masks = []
        cntIntro = {}
        cntExtro = {}
        innerScore = {}
        
        for mask in range(3**n):
            arr = []
            x = mask
            i_count = e_count = 0
            for _ in range(n):
                d = x % 3
                arr.append(d)
                if d == 1:
                    i_count += 1
                elif d == 2:
                    e_count += 1
                x //= 3
            if i_count > introvertsCount or e_count > extrovertsCount:
                continue
            score = 0
            for j, d in enumerate(arr):
                if d == 1:
                    score += 120
                elif d == 2:
                    score += 40
                if j > 0 and arr[j-1] and d:
                    # horizontal neighbor effect
                    score += (-30 if arr[j-1]==1 else 20)
                    score += (-30 if d==1 else 20)
            masks.append(mask)
            cntIntro[mask] = i_count
            cntExtro[mask] = e_count
            innerScore[mask] = score
        
        # 2) Precompute vertical crossârow scores
        crossScore = {pm: {} for pm in masks}
        power3 = [3**i for i in range(n)]
        for pm in masks:
            for cm in masks:
                s = 0
                for j in range(n):
                    d0 = (pm // power3[j]) % 3
                    d1 = (cm // power3[j]) % 3
                    if d0 and d1:
                        s += (-30 if d0==1 else 20)
                        s += (-30 if d1==1 else 20)
                crossScore[pm][cm] = s
        
        # 3) Memoized recursion without functools
        memo = {}
        full_mask = 0  # not used but placeholder
        
        def dp(r, ic, ec, pmask):
            key = (r, ic, ec, pmask)
            if key in memo:
                return memo[key]
            if r == m:
                return 0
            best = 0
            for cm in masks:
                ci = cntIntro[cm]
                ce = cntExtro[cm]
                if ci <= ic and ce <= ec:
                    val = innerScore[cm] + crossScore[pmask][cm] + dp(r+1, ic-ci, ec-ce, cm)
                    if val > best:
                        best = val
            memo[key] = best
            return best
        
        return dp(0, introvertsCount, extrovertsCount, 0)
