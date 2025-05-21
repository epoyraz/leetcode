from collections import Counter

class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)
        changed.sort()
        original = []

        for x in changed:
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return []
            if x == 0 and count[x] < 2:
                return []
            original.append(x)
            count[x] -= 1
            count[2 * x] -= 1

        return original
