class Solution:
    def minimumCardPickup(self, cards):
        last = {}
        ans = float('inf')
        for i, x in enumerate(cards):
            if x in last:
                # length from last[x] to i inclusive
                ans = min(ans, i - last[x] + 1)
            last[x] = i
        return ans if ans != float('inf') else -1
