class Solution(object):
    def maxIncreasingGroups(self, usageLimits):
        usageLimits.sort()
        available = 0      # running count of still-unassigned copies
        size = 0           # current group size we need to form next (also the answer so far)

        for c in usageLimits:
            available += c
            if available >= size + 1:   # can we build the next larger group?
                size += 1
                available -= size       # consume items for this group

        return size
