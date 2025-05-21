from bisect import bisect_right
from collections import defaultdict

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.times = times
        self.lead = []
        
        count = defaultdict(int)
        current_lead = None
        max_count = 0
        
        for p in persons:
            count[p] += 1
            # if this candidate ties or exceeds the max, they become the leader
            if count[p] >= max_count:
                current_lead = p
                max_count = count[p]
            self.lead.append(current_lead)

    def q(self, t):
        # find rightmost vote time <= t
        idx = bisect_right(self.times, t) - 1
        return self.lead[idx]
