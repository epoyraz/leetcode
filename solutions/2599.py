class Solution:
    def takeCharacters(self, s, k):
        from collections import Counter

        total = Counter(s)
        # If any character has fewer than k in total, impossible.
        if any(total[c] < k for c in 'abc'):
            return -1

        n = len(s)
        # Limits on how many of each char we can remove in the middle window:
        limit = {c: total[c] - k for c in 'abc'}

        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        max_window = 0

        # Slide right pointer
        for right, ch in enumerate(s):
            count[ch] += 1
            # If window [left..right] is invalid (removed too many of some char),
            # shrink from the left until valid again.
            while any(count[c] > limit[c] for c in 'abc'):
                count[s[left]] -= 1
                left += 1
            # Now [left..right] is a valid removable window
            max_window = max(max_window, right - left + 1)

        # Minimum taken = total length - max removable window
        return n - max_window
