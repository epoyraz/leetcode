class Solution:
    def numberOfArrays(self, differences, lower, upper):
        curr = 0
        min_val = 0
        max_val = 0

        for diff in differences:
            curr += diff
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)

        total_range = upper - lower
        needed_range = max_val - min_val

        return max(0, total_range - needed_range + 1)
