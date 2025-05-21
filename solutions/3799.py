from collections import Counter
from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        count = 0
        seen = set()
        digit_counter = Counter(digits)

        for perm in permutations(digits, 3):
            if perm[0] == 0 or perm[2] % 2 != 0:
                continue
            if perm in seen:
                continue
            if all(Counter(perm)[d] <= digit_counter[d] for d in perm):
                seen.add(perm)
                count += 1

        return count
