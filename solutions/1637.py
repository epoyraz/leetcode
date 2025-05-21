class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        memo = {}

        def getLength(count):
            if count == 1:
                return 1
            elif count < 10:
                return 2
            elif count < 100:
                return 3
            else:
                return 4

        def dp(i, k):
            if k < 0:
                return float('inf')
            if i == len(s):
                return 0
            if (i, k) in memo:
                return memo[(i, k)]

            res = float('inf')
            count = 0
            del_count = 0

            for j in range(i, len(s)):
                if s[j] == s[i]:
                    count += 1
                else:
                    del_count += 1

                if del_count > k:
                    break

                res = min(res, getLength(count) + dp(j + 1, k - del_count))

            # Option to delete s[i]
            res = min(res, dp(i + 1, k - 1))

            memo[(i, k)] = res
            return res

        return dp(0, k)
