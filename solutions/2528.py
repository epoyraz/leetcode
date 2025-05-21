class Solution(object):
    def countTime(self, time):
        # time = "hh:mm"
        h1, h2, _, m1, m2 = time
        
        # Count hour possibilities
        if h1 == '?' and h2 == '?':
            hours = 24
        elif h1 == '?':
            d2 = int(h2)
            hours = 3 if d2 <= 3 else 2
        elif h2 == '?':
            d1 = int(h1)
            hours = 10 if d1 <= 1 else 4
        else:
            hours = 1
        
        # Count minute possibilities
        if m1 == '?' and m2 == '?':
            minutes = 60
        elif m1 == '?':
            minutes = 6
        elif m2 == '?':
            minutes = 10
        else:
            minutes = 1
        
        return hours * minutes
