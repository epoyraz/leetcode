class Solution:
    def circularGameLosers(self, n, k):
        seen = set()
        current = 0  # 0-based index for friend 1
        i = 1  # round count multiplier
        while current not in seen:
            seen.add(current)
            current = (current + i * k) % n
            i += 1
        return sorted([j + 1 for j in range(n) if j not in seen])
