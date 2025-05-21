class Solution(object):
    def numberOfWeeks(self, milestones):
        total = sum(milestones)
        m = max(milestones)
        rest = total - m
        # If the largest project can be interleaved with the rest, do all weeks
        if m <= rest + 1:
            return total
        # Otherwise, we can only alternate until others run out
        return rest * 2 + 1
