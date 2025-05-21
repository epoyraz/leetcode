class Solution:
    def stoneGameVIII(self, stones):
        # n stones, stones[i] values
        n = len(stones)
        # prefix sums: pre[i] = sum of stones[0..i]
        pre = [0] * n
        pre[0] = stones[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + stones[i]
        # if only 2 stones, Alice must take both at once
        if n == 2:
            return pre[1]
        # dp = best score difference starting when only pre[i..] matter
        # initialize dp at last index = pre[n-1]
        dp = pre[n - 1]
        # iterate i = n-2 down to 1
        for i in range(n - 2, 0, -1):
            # either skip this prefix (dp stays), or take prefix up to i:
            # Alice gets pre[i], then Bob plays optimally giving dp next,
            # so net = pre[i] - dp.
            dp = max(dp, pre[i] - dp)
        # dp at i=1 is the answer
        return dp
