class Solution(object):
    def countWays(self, ranges):
        MOD = 10**9 + 7

        # Step 1: Sort by start
        ranges.sort()

        count = 0
        end = -1

        # Step 2: Merge overlapping intervals
        for start, stop in ranges:
            if start > end:
                count += 1  # new component
                end = stop
            else:
                end = max(end, stop)

        # Step 3: Return 2^count % MOD
        return pow(2, count, MOD)
