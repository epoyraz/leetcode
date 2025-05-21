class Solution(object):
    def minimumSeconds(self, nums):
        from collections import defaultdict

        n = len(nums)
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        best = float('inf')
        for indices in pos.values():
            indices.sort()
            max_gap = 0
            k = len(indices)
            for i in range(k):
                j = (i + 1) % k
                # number of untouched slots between indices[i] and indices[j]
                gap = (indices[j] - indices[i] - 1) % n
                max_gap = max(max_gap, gap)
            # each second the two ends of a gap move inward by 1 total,
            # so it takes ceil(gap/2) = (gap+1)//2 seconds to fill
            best = min(best, (max_gap + 1) // 2)

        return best
