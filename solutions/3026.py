class Solution(object):
    def minimumPossibleSum(self, n, target):
        mod = 10**9 + 7

        # Number of disjoint âconflictâpairsâ below target:
        # pairs (i, targetâi) for i=1..floor((targetâ1)/2)
        L = (target - 1) // 2

        # Sum of the âsafeâ smaller side of each pair: 1 + 2 + â¦ + L
        sumA = L * (L + 1) // 2

        # If target is even, the middle value target/2 stands alone (no conflict).
        hasMid = 1 if target % 2 == 0 else 0
        mid = target // 2 if hasMid else 0

        if n <= L:
            # We only need the first n integers 1..n
            return (n * (n + 1) // 2) % mod

        if n <= L + hasMid:
            # We take all L âsmallâ picks plus the single middle
            return (sumA + mid) % mod

        # Otherwise we take:
        #  â¢ All L âsmallâ picks,
        #  â¢ The middle (if any),
        #  â¢ Plus r more integers starting from target upwards.
        r = n - L - hasMid
        # Sum of r consecutive numbers target, target+1, â¦, target+râ1:
        sumB = r * (2*target + (r - 1)) // 2

        return (sumA + mid + sumB) % mod
