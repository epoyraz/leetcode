class Solution(object):
    def largestPalindrome(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        Returns the largest n-digit palindrome divisible by k.
        """
        # Special case for k == 1: all 9's
        if k == 1:
            return '9' * n
        # Compute half-length and whether there's a middle digit
        half = n // 2
        has_mid = (n % 2 == 1)
        L = half + (1 if has_mid else 0)
        # Precompute powers of 10 mod k up to n
        pow10 = [0] * (n + 1)
        pow10[0] = 1 % k
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % k
        # Build weight array W for positions 0..L-1
        W = [0] * L
        for i in range(half):
            # weight is 10^{n-1-i} + 10^{i} (mod k)
            W[i] = (pow10[n-1-i] + pow10[i]) % k
        if has_mid:
            # middle position contributes 10^{half}
            W[half] = pow10[half] % k
        # DP table: dp[pos][rem] = can suffix from pos..L-1 achieve sum mod k == rem
        dp = [ [False] * k for _ in range(L+1) ]
        dp[L][0] = True
        # Fill DP backwards
        for pos in range(L-1, -1, -1):
            w = W[pos]
            for rem in range(k):
                # Try all digits
                d_start = 1 if pos == 0 else 0
                for d in range(d_start, 10):
                    need = (rem - d * w) % k
                    if dp[pos+1][need]:
                        dp[pos][rem] = True
                        break
        # If not possible at all, return "" (or could return "0" * n)
        if not dp[0][0]:
            return ""
        # Greedy construct digits
        digits = [0] * L
        rem = 0
        for pos in range(L):
            w = W[pos]
            d_start = 1 if pos == 0 else 0
            for d in range(9, d_start-1, -1):
                need = (rem - d * w) % k
                if dp[pos+1][need]:
                    digits[pos] = d
                    rem = need
                    break
        # Build palindrome string
        left = ''.join(str(d) for d in digits[:half])
        mid = str(digits[half]) if has_mid else ''
        right = left[::-1]
        return left + mid + right