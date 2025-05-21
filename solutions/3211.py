import heapq

class Solution(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 1) Build prefix sums P
        P = [0] * (n + 1)
        for i, v in enumerate(nums, start=1):
            P[i] = P[i-1] + v

        # heap:   (T_j,   dp[j]-j,   -P[j],   j)
        # pq:     (dp[j]-j,  -P[j],   j)
        heap = []
        pq   = []

        # Base state j=0: dp[0]=0, last_sum[0]=0, so T0 = 0 + 0 = 0
        heapq.heappush(heap, (0, 0, 0, 0))

        dp_n = None

        for i in range(1, n+1):
            # 2) move all states with T_j <= P[i] into pq
            while heap and heap[0][0] <= P[i]:
                Tj, dpj_j, negPj, j = heapq.heappop(heap)
                heapq.heappush(pq, (dpj_j, negPj, j))

            if not pq:
                # Should never happen (j=0 is always eligible once i>=1),
                # but if it did, we'd have to merge everything â 1 segment.
                dp_i = i - 1
            else:
                dpj_j, negPj, j = pq[0]
                # dp[i] = dp[j] + (i - j - 1)
                dp_i = (i - 1) + dpj_j

            if i == n:
                dp_n = dp_i

            # Compute last_sum[i] = sum(nums[j..i-1]) = P[i]-P[j]
            # where j is the argmin we just used (or 0 if pq was empty).
            # In the empty-pq fallback, j=0 and dpj_j=0 by construction.
            if pq:
                Pj = -negPj
            else:
                Pj = 0
            last_sum_i = P[i] - Pj

            # New state's T_i = P[i] + last_sum_i
            T_i = P[i] + last_sum_i
            # And dp[i] - i = dpj_j - 1  (check: (i-1+dpj_j)-i = dpj_j-1)
            dp_i_minus_i = dpj_j - 1 if pq else -1

            heapq.heappush(heap, (T_i, dp_i_minus_i, -P[i], i))

        # dp_n is the minimum #merges. #segments = n - #merges.
        return n - dp_n
