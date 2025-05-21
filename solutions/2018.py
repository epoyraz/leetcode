import bisect

class Solution:
    def minWastedSpace(self, packages, boxes):
        MOD = 10**9 + 7
        packages.sort()
        prefix = [0]
        for p in packages:
            prefix.append(prefix[-1] + p)
        
        res = float('inf')
        
        for supplier in boxes:
            supplier.sort()
            if supplier[-1] < packages[-1]:
                continue  # can't fit all packages
            i = 0
            total = 0
            for b in supplier:
                j = bisect.bisect_right(packages, b, i)
                count = j - i
                total += b * count - (prefix[j] - prefix[i])
                i = j
                if i == len(packages):
                    break
            res = min(res, total)
        
        return res % MOD if res < float('inf') else -1
