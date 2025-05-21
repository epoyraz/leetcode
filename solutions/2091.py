from array import array

class Solution(object):
    def numberOfCombinations(self, num):
        mod = 10**9 + 7
        n = len(num)
        if n == 0 or num[0] == '0':
            return 0

        # 1) Build LCP table (size (n+1)x(n+1)) using 16-bit ints
        #    lcp[i][j] = length of longest common prefix of num[i:] and num[j:]
        lcp = [array('H', [0]) * (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            row_i    = lcp[i]
            row_ip1  = lcp[i+1]
            num_i    = num[i]
            for j in range(n-1, -1, -1):
                if num_i == num[j]:
                    row_i[j] = row_ip1[j+1] + 1

        def le(i, j, length):
            # return True if num[i:i+length] <= num[j:j+length]
            common = lcp[i][j]
            if common >= length:
                return True
            return num[i+common] < num[j+common]

        # 2) prefix[i][k] = sum of dp[i][1..k], stored as 32-bit ints
        prefix = [array('I', [0]) * (n+1) for _ in range(n+1)]

        # 3) Fill DP by increasing i = end of string
        for i in range(1, n+1):
            row_i = prefix[i]
            for length in range(1, i+1):
                j = i - length
                ways = 0
                if num[j] != '0':
                    if j == 0:
                        # the very first block
                        ways = 1
                    else:
                        # sum of all dp[j][â'] for â' < length
                        max_short = length - 1 if length - 1 <= j else j
                        ways = prefix[j][max_short]
                        # plus same-length case if non-decreasing
                        if j >= length and le(j-length, j, length):
                            dp_j_len = prefix[j][length] - prefix[j][length-1]
                            ways = (ways + dp_j_len) % mod

                # build prefix sum for this row
                row_i[length] = (row_i[length-1] + ways) % mod

        # answer is sum of dp[n][1..n], i.e. prefix[n][n]
        return prefix[n][n]
