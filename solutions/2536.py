class Solution(object):
    def haveConflict(self, event1, event2):
        def to_minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        
        s1 = to_minutes(event1[0])
        e1 = to_minutes(event1[1])
        s2 = to_minutes(event2[0])
        e2 = to_minutes(event2[1])
        
        # They conflict if the later start is <= the earlier end
        return max(s1, s2) <= min(e1, e2)
