class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        """
        :type nums: List[int]
        :type k: int
        :type op1: int
        :type op2: int
        :rtype: int
        """
        n = len(nums)
        # Precompute gains at each index
        items = []
        for v in nums:
            # gain of op1 alone
            s1 = v - ((v + 1) // 2)        # = floor(v/2)
            # gain of op2 alone, only if v>=k
            s2 = k if v >= k else None

            # gain of doing both: try both orders
            best_both = None

            # op1 then op2
            v1 = (v + 1)//2
            if v1 >= k:
                gA = v - (v1 - k)
                best_both = gA

            # op2 then op1
            if v >= k:
                v2 = v - k
                gB = v - ((v2+1)//2)
                best_both = max(best_both, gB) if best_both is not None else gB

            items.append((s1, s2, best_both))

        # dp[c1][c2] = max gain using <=c1 of op1 and <=c2 of op2
        NEG = -10**18
        dp = [[NEG]*(op2+1) for _ in range(op1+1)]
        dp[0][0] = 0

        for (s1, s2, sb) in items:
            new_dp = [row[:] for row in dp]
            for c1 in range(op1+1):
                for c2 in range(op2+1):
                    base = dp[c1][c2]
                    if base < 0:
                        continue
                    # op1 only
                    if s1 > 0 and c1+1 <= op1:
                        new_dp[c1+1][c2] = max(new_dp[c1+1][c2], base + s1)
                    # op2 only
                    if s2 is not None and s2 > 0 and c2+1 <= op2:
                        new_dp[c1][c2+1] = max(new_dp[c1][c2+1], base + s2)
                    # both
                    if sb is not None and sb > 0 and c1+1 <= op1 and c2+1 <= op2:
                        new_dp[c1+1][c2+1] = max(new_dp[c1+1][c2+1], base + sb)
            dp = new_dp

        # maximum gain is the best over all (i,j) within limits
        max_gain = max(dp[c1][c2] 
                       for c1 in range(op1+1) 
                       for c2 in range(op2+1))
        return sum(nums) - max_gain
