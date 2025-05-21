from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        ans = 0

        for i, x in enumerate(keys):
            for j, y in enumerate(keys[i:], i):
                z = target - x - y
                if z < y:
                    continue
                if z not in count:
                    continue

                cx, cy, cz = count[x], count[y], count[z]

                if x == y == z:
                    ans += cx * (cx - 1) * (cx - 2) // 6
                elif x == y != z:
                    ans += cx * (cx - 1) // 2 * cz
                elif x < y == z:
                    ans += cx * cy * (cy - 1) // 2
                elif x < y < z:
                    ans += cx * cy * cz

                ans %= MOD

        return ans
