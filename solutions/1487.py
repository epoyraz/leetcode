class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        from collections import defaultdict

        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            reserved[row].add(seat)

        result = 0
        for row in reserved:
            seats = reserved[row]
            count = 0
            if not (2 in seats or 3 in seats or 4 in seats or 5 in seats):
                count += 1
            if not (6 in seats or 7 in seats or 8 in seats or 9 in seats):
                count += 1
            if count == 0 and not (4 in seats or 5 in seats or 6 in seats or 7 in seats):
                count = 1
            result += count

        return result + (n - len(reserved)) * 2
