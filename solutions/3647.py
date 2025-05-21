import heapq

class Solution(object):
    def maxRemoval(self, nums, queries):
        n = len(nums)
        q = len(queries)

        # 1) bucket by left endpoint
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)

        available = []      # max-heap (store -r) of intervals we could still pick
        selected_ends = []  # min-heap of râs for intervals we've already picked
        cov = 0             # how many picked intervals currently cover i
        picked = 0

        for i in range(n):
            # add everything starting here
            for r in starts[i]:
                heapq.heappush(available, -r)

            # expire any picked intervals that ended before i
            while selected_ends and selected_ends[0] < i:
                heapq.heappop(selected_ends)
                cov -= 1

            # if we still need more coverage at i, pick greedily
            while cov < nums[i]:
                # drop any available intervals that don't reach i
                while available and -available[0] < i:
                    heapq.heappop(available)
                if not available:
                    return -1
                r = -heapq.heappop(available)
                picked += 1
                cov += 1
                heapq.heappush(selected_ends, r)

        return q - picked
