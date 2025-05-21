class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        n = len(receiver)
        # Maximum power for k up to 1e10 -> log2(k) ~ 34
        LOG = k.bit_length()  # enough bits to cover k
        # up[i][j] = node reached from i after 2^j passes
        up = [[0]*LOG for _ in range(n)]
        # sumUp[i][j] = sum of the indices of the 2^j nodes we pass through
        # starting from i (excluding i itself, including the 2^j-th node)
        sumUp = [[0]*LOG for _ in range(n)]

        # Initialize 2^0 = 1 pass
        for i in range(n):
            nxt = receiver[i]
            up[i][0] = nxt
            sumUp[i][0] = nxt  # one pass lands on nxt

        # Build binary lifting tables
        for j in range(1, LOG):
            for i in range(n):
                mid = up[i][j-1]
                up[i][j] = up[mid][j-1]
                # sum of first 2^j passes = sum of first 2^(j-1) + 
                # then from the mid node another 2^(j-1) passes
                sumUp[i][j] = sumUp[i][j-1] + sumUp[mid][j-1]

        ans = 0
        # For each starting i, compute sum over k passes
        for i in range(n):
            total = i  # include the starting player
            curr = i
            rem = k
            b = 0
            while rem > 0:
                if rem & 1:
                    total += sumUp[curr][b]
                    curr = up[curr][b]
                rem >>= 1
                b += 1
            if total > ans:
                ans = total

        return ans
