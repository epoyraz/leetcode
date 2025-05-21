import itertools
import bisect

class Solution(object):
    def nextBeautifulNumber(self, n):
        # Step 1: Build all balanced numbers of up to 7 digits
        balanced = set()
        # For each subset of digits 1..9, decide which digits to include
        # A digit d, if included, must appear exactly d times
        for mask in range(1, 1<<9):
            digits = []
            length = 0
            for d in range(1, 10):
                if (mask >> (d-1)) & 1:
                    length += d
                    digits += [str(d)] * d
            # we only need numbers up to 7 digits (since n â¤ 10^6)
            if 1 <= length <= 7:
                # generate all unique permutations of this multiset
                for perm in set(itertools.permutations(digits, length)):
                    # skip those starting with '0' (none will, since digits are '1'..'9')
                    num = int("".join(perm))
                    balanced.add(num)

        # Step 2: Sort the list
        sorted_balanced = sorted(balanced)

        # Step 3: Binary-search for the smallest > n
        idx = bisect.bisect_right(sorted_balanced, n)
        return sorted_balanced[idx]
