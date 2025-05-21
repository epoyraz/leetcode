class Solution:
    def minCost(self, nums, k):
        n = len(nums)
        INF = 10**30
        dp = [INF] * (n + 1)
        dp[0] = 0

        # We'll reuse a freq array of size n (nums[i] < n by constraint).
        freq = [0] * n

        for j in range(n):
            # reset freq and trimmedLen for the new start j
            trimmedLen = 0
            # zero out only the used entries: we'll keep track of which we touched
            used = []

            for i in range(j, n):
                x = nums[i]
                f = freq[x]
                if f == 0:
                    freq[x] = 1
                    used.append(x)
                elif f == 1:
                    # first time we reach count 2
                    freq[x] = 2
                    trimmedLen += 2
                else:
                    # f >= 2
                    freq[x] += 1
                    trimmedLen += 1

                cost = k + trimmedLen
                # update dp for prefix ending at i
                if dp[j] + cost < dp[i + 1]:
                    dp[i + 1] = dp[j] + cost

            # clear freq for all touched values
            for x in used:
                freq[x] = 0
            # also reset those that went >=2
            # (they appear in used as well, since we appended on f==0 only)
            # but to be safe:
            for i2 in range(j, n):
                x = nums[i2]
                if freq[x] > 0:
                    freq[x] = 0

        return dp[n]
