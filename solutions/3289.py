class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        n, m = len(nums), len(changeIndices)
        base = n + sum(nums)                        # cost with no âsetâ

        # ---------- helper that tests if we can finish in `s` seconds ----------
        def ok(s):
            need = base - s                         # seconds we still have to save
            if need <= 0:                           # already enough time
                return True

            # first appearance (1-based) of every index in the range [1, s-1]
            first = [-1] * n
            for t in range(s - 1):                  # we cannot âsetâ at second s
                i = changeIndices[t] - 1
                if first[i] == -1:
                    first[i] = t + 1

            # candidates = (saving, position) for indices with nums[i] > 1
            cand = [(-(nums[i] - 1), first[i])
                     for i in range(n)
                     if nums[i] > 1 and first[i] != -1]
            cand.sort()                             # biggest saving first

            from bisect import bisect_left, insort
            chosen = []                             # positions of selected âsetâs
            saved  = 0

            for neg_save, pos in cand:
                insort(chosen, pos)                 # try to take this âsetâ
                # check the spacing condition:
                # for every suffix, #sets â¤ free seconds in that suffix
                ok_here, k = True, len(chosen)
                cnt = 0
                for p in reversed(chosen):          # iterate suffix sizes
                    cnt += 1                        # sets in this suffix
                    if 2 * cnt - 1 > s - p:        # not enough room for marks
                        ok_here = False
                        break
                if not ok_here:                     # keep schedule valid
                    chosen.pop(bisect_left(chosen, pos))
                    continue

                saved += -neg_save                  # add this saving
                if saved >= need:                  # reached required saving
                    return True
            return False

        # ---------------- binary-search the answer ----------------
        lo, hi, ans = 1, m, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi  = mid - 1
            else:
                lo  = mid + 1
        return ans
