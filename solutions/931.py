from collections import defaultdict

class FreqStack(object):
    def __init__(self):
        self.freq = defaultdict(int)       # Maps val -> frequency
        self.group = defaultdict(list)     # Maps frequency -> list of values
        self.maxfreq = 0                   # Current maximum frequency

    def push(self, val):
        f = self.freq[val] + 1
        self.freq[val] = f
        self.group[f].append(val)
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self):
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
