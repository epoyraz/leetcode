from collections import defaultdict

class Solution:
    def distance(self, nums):
        index_map = defaultdict(list)
        for i, val in enumerate(nums):
            index_map[val].append(i)

        res = [0] * len(nums)

        for positions in index_map.values():
            prefix = [0]
            for pos in positions:
                prefix.append(prefix[-1] + pos)

            m = len(positions)
            for idx, pos in enumerate(positions):
                left = idx
                right = m - 1 - idx
                sum_left = prefix[idx]
                sum_right = prefix[-1] - prefix[idx + 1]
                res[pos] = pos * left - sum_left + sum_right - pos * right

        return res
