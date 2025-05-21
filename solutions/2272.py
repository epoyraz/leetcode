class Solution:
    def maximumGood(self, statements):
        n = len(statements)
        ans = 0

        for mask in range(1 << n):  # Try all combinations of people being good/bad
            valid = True
            for i in range(n):
                if not (mask >> i) & 1:
                    continue  # i is not assumed to be good, skip

                for j in range(n):
                    if statements[i][j] == 2:
                        continue
                    if statements[i][j] == 1 and not ((mask >> j) & 1):
                        valid = False  # Good person i says j is good but j is not in the mask
                    if statements[i][j] == 0 and ((mask >> j) & 1):
                        valid = False  # Good person i says j is bad but j is in the mask
            if valid:
                ans = max(ans, bin(mask).count('1'))

        return ans
