from collections import Counter

class Solution:
    def recoverArray(self, n, sums):
        sums = list(sums)
        ans = []

        for _ in range(n):
            sums.sort()
            diff = sums[1] - sums[0]          # candidate element (non-negative)

            cnt = Counter(sums)
            without, with_elem = [], []

            for s in sums:                     # split into âwithoutâ and âwith diffâ
                if cnt[s] == 0:
                    continue
                cnt[s] -= 1
                t = s + diff
                cnt[t] -= 1
                without.append(s)
                with_elem.append(t)

            if 0 in without:                   # 0 is always in the group w/o the element
                ans.append(diff)
                sums = without
            else:                              # otherwise the element is âdiff
                ans.append(-diff)
                sums = with_elem

        return ans
