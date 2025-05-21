import heapq

class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        P = len(conflictingPairs)
        # For each pair, store (l, r-1) and an ID
        by_l = [[] for _ in range(n+2)]
        for pid, (a, b) in enumerate(conflictingPairs):
            l, r = min(a, b), max(a, b)
            by_l[l].append((r-1, pid))

        heap = []  # will store (r-1, pid)
        baseline = 0
        # For each pair ID, track total delta when removed
        delta = [0]*P

        # Process i = n down to 1
        for i in range(n, 0, -1):
            # add all pairs whose l == i
            for item in by_l[i]:
                heapq.heappush(heap, item)

            # find best1 and best2 among current heap
            if not heap:
                best1 = best2 = n
                pid1 = -1
            else:
                # pop smallest
                r1, pid1 = heapq.heappop(heap)
                best1 = r1
                if heap:
                    best2 = heap[0][0]
                else:
                    best2 = n
                # push back
                heapq.heappush(heap, (r1, pid1))

            # limit for subarrays starting at i is up to min(best1, n)
            end = min(best1, n)
            if end >= i:
                baseline += (end - i + 1)

            # if this best1 came from a real pair, record its effect
            if pid1 >= 0:
                # removing that pair would raise limit from best1 to best2
                # so #subarrays from i rises by (best2 - best1)
                delta[pid1] += (best2 - best1)

        # The best we can do is remove the pair with max delta
        best_extra = max(0, max(delta))
        return baseline + best_extra
