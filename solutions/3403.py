class Solution(object):
    def minimumSubstringsInPartition(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i] = min # of balanced substrings covering s[:i]
        dp = [10**9] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            count = [0]*26
            distinct = 0
            maxf = 0
            # try all j ending at i
            for j in range(i, 0, -1):
                idx = ord(s[j-1]) - ord('a')
                if count[idx] == 0:
                    distinct += 1
                count[idx] += 1
                if count[idx] > maxf:
                    maxf = count[idx]

                length = i - j + 1
                # balanced <=> all freq equal => maxf * distinct == length
                if maxf * distinct == length:
                    # we can cut here
                    if dp[j-1] + 1 < dp[i]:
                        dp[i] = dp[j-1] + 1
            # end for j
        # end for i

        return dp[n]
