class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Step 1: Compute LCS
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)

        # Step 2: Build SCS from LCS
        lcs = dp[m][n]
        i = j = 0
        result = []

        for c in lcs:
            while str1[i] != c:
                result.append(str1[i])
                i += 1
            while str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1

        # Add remaining characters
        result.extend(str1[i:])
        result.extend(str2[j:])
        return ''.join(result)
