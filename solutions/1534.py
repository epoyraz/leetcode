class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        from collections import defaultdict

        counts = {'c': 0, 'r': 0, 'o': 0, 'a': 0}
        max_frogs = 0
        current_frogs = 0

        for ch in croakOfFrogs:
            if ch == 'c':
                counts['c'] += 1
                current_frogs += 1
                max_frogs = max(max_frogs, current_frogs)
            elif ch == 'r':
                if counts['c'] == 0:
                    return -1
                counts['c'] -= 1
                counts['r'] += 1
            elif ch == 'o':
                if counts['r'] == 0:
                    return -1
                counts['r'] -= 1
                counts['o'] += 1
            elif ch == 'a':
                if counts['o'] == 0:
                    return -1
                counts['o'] -= 1
                counts['a'] += 1
            elif ch == 'k':
                if counts['a'] == 0:
                    return -1
                counts['a'] -= 1
                current_frogs -= 1
            else:
                return -1  # invalid character

        # If any frogs are still mid-croak, it's invalid
        if any(counts[ch] > 0 for ch in 'croa'):
            return -1

        return max_frogs
