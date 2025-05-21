import bisect

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        full = {}           # Map from lake -> index of last full day
        dry_days = []       # Indices of dry days
        res = [-1] * len(rains)

        for i in range(len(rains)):
            lake = rains[i]
            if lake == 0:
                dry_days.append(i)
                res[i] = 1  # Default, will be updated if needed
            else:
                if lake in full:
                    # Need to dry lake before today
                    prev_day = full[lake]
                    idx = bisect.bisect_right(dry_days, prev_day)
                    if idx == len(dry_days):
                        return []  # No day to dry the lake â flood
                    dry_day = dry_days[idx]
                    res[dry_day] = lake
                    dry_days.pop(idx)
                full[lake] = i  # Mark lake as full

        return res
