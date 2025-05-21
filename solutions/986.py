from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr):
        max_time = -1
        
        # Try every permutation of the 4 digits
        for h1, h2, m1, m2 in permutations(arr):
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            # Check if valid time
            if 0 <= hours < 24 and 0 <= minutes < 60:
                total = hours * 60 + minutes
                if total > max_time:
                    max_time = total
        
        if max_time < 0:
            return ""
        
        hh = max_time // 60
        mm = max_time % 60
        # Format with leading zeros without using f-strings
        return "{:02d}:{:02d}".format(hh, mm)
