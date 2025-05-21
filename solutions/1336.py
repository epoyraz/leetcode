import heapq

class Solution(object):
    def maxProduct(self, s):
        n = len(s)
        # Manacher's odd-length radii
        d1 = [0]*n
        l = r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l+r-i], r - i + 1)
            while i-k >= 0 and i+k < n and s[i-k] == s[i+k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # Compute best_left[i]: max odd-pal length ending at or before i
        best_left = [0]*n
        heap = []  # min-heap of (center, right_end)
        for i in range(n):
            # Add center i
            c = i
            end = c + d1[c] - 1
            if d1[c] > 0:
                heapq.heappush(heap, (c, end))
            # Remove expired centers
            while heap and heap[0][1] < i:
                heapq.heappop(heap)
            # Choose minimal center among active
            curr = 0
            if heap:
                c0, _ = heap[0]
                curr = 2*(i - c0 + 1) - 1
            best_left[i] = curr if i == 0 else max(best_left[i-1], curr)

        # Compute best_right[i]: max odd-pal length starting at or after i
        best_right = [0]*n
        heap = []
        for i in range(n-1, -1, -1):
            c = i
            # for right side, center c covers start = c - (d1[c]-1)
            start = c - (d1[c] - 1)
            if d1[c] > 0:
                heapq.heappush(heap, (-c, start))
            # Remove expired (start > i) => intervals not covering i
            while heap and heap[0][1] > i:
                heapq.heappop(heap)
            curr = 0
            if heap:
                # maximal palindrome uses maximal center => minimal -c
                c0 = -heap[0][0]
                curr = 2*(c0 - i + 1) - 1
            best_right[i] = curr if i == n-1 else max(best_right[i+1], curr)

        # Maximize product over split
        ans = 0
        for i in range(n-1):
            ans = max(ans, best_left[i] * best_right[i+1])
        return ans
