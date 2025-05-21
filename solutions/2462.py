import heapq

class Solution(object):
    def kSum(self, nums, k):
        # 1) Maximum subsequence sum = sum of positives.
        total = sum(x for x in nums if x > 0)
        # 2) Sort abs values so we peel off the smallest contributions first.
        abs_sorted = sorted(abs(x) for x in nums)
        n = len(abs_sorted)

        # Max-heap via negation: entries are (-current_sum, idx)
        heap = [(-total, 0)]
        # Track visited (idx, current_sum) to avoid duplicates
        visited = {(0, total)}

        ans = total
        for _ in range(k):
            if not heap:
                # No more new states: remaining sums all == ans
                break

            neg_curr, i = heapq.heappop(heap)
            curr = -neg_curr
            ans = curr

            # Generate next states by âremovingâ abs_sorted[i]
            if i < n:
                # A) Simply subtract abs_sorted[i]
                s1 = curr - abs_sorted[i]
                state1 = (i + 1, s1)
                if state1 not in visited:
                    visited.add(state1)
                    heapq.heappush(heap, (-s1, i + 1))

                # B) If i>0, swap out the previous removal for this one
                if i > 0:
                    s2 = curr - abs_sorted[i] + abs_sorted[i - 1]
                    state2 = (i + 1, s2)
                    if state2 not in visited:
                        visited.add(state2)
                        heapq.heappush(heap, (-s2, i + 1))

        return ans
