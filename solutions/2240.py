from collections import defaultdict
import bisect

class Solution:
    def getDistances(self, arr):
        pos = defaultdict(list)
        for i, val in enumerate(arr):
            pos[val].append(i)

        res = [0] * len(arr)

        for indices in pos.values():
            prefix = [0] * (len(indices) + 1)
            for i in range(len(indices)):
                prefix[i + 1] = prefix[i] + indices[i]

            for i, idx in enumerate(indices):
                left = i * idx - prefix[i]
                right = (prefix[-1] - prefix[i + 1]) - (len(indices) - i - 1) * idx
                res[idx] = left + right

        return res
