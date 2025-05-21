import heapq

class Solution(object):
    def resultsArray(self, queries, k):
        # max-heap (as min-heap of negatives) for the k smallest distances
        small = []
        # min-heap for the remaining distances
        large = []
        res = []

        for x, y in queries:
            d = abs(x) + abs(y)
            if len(small) < k:
                # still need more to reach k
                heapq.heappush(small, -d)
            else:
                # small is full (size == k)
                # compare with the largest in small (i.e. -small[0])
                if -small[0] > d:
                    # new distance is among the k smallest
                    heapq.heappush(small, -d)
                    # pop the largest from small into large
                    moved = -heapq.heappop(small)
                    heapq.heappush(large, moved)
                else:
                    # goes into the "rest"
                    heapq.heappush(large, d)

            # if fewer than k obstacles so far
            if len(small) < k:
                res.append(-1)
            else:
                # the kth smallest is the max of 'small'
                res.append(-small[0])

        return res
