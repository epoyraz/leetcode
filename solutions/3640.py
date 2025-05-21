from collections import Counter

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        n = len(nums)
        freq = Counter(nums)
        events = []
        for v in nums:
            L = v - k
            R = v + k
            events.append((L, 1))
            events.append((R + 1, -1))
        events.sort()
        queries = sorted(freq)
        cnt_cover = {}
        C = 0
        i = 0
        best_cover = 0
        for q in queries:
            while i < len(events) and events[i][0] <= q:
                C += events[i][1]
                i += 1
            cnt_cover[q] = C
        while i < len(events):
            C += events[i][1]
            i += 1
        best_cover = 0
        curr = 0
        for pos, delta in events:
            curr += delta
            if curr > best_cover:
                best_cover = curr
        ans = min(best_cover, numOperations)
        for t, c0 in freq.items():
            c = cnt_cover.get(t, 0)
            val = c0 + (numOperations if c - c0 >= numOperations else c - c0)
            if val > ans:
                ans = val
        return ans
