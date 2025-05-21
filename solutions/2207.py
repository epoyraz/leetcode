import heapq


class SORTracker:
    MAX_LEN = 10          # given in the constraints

    def __init__(self):
        self.small = []   # (score, inv_name_padded, name)  â worst of top-k on top
        self.large = []   # (-score, name)                 â best of the rest on top
        self.k = 0        # how many times get() has been called

    # -------------------------- helpers ---------------------------------
    def _inv_pad(self, name):
        """invert letters and right-pad with 0xff so longer names rank *worse*"""
        inv = ''.join(chr(255 - ord(c)) for c in name)
        return inv + '\xff' * (self.MAX_LEN - len(name))

    # --------------------------- API ------------------------------------
    def add(self, name, score):
        # â  insert into 'large'
        heapq.heappush(self.large, (-score, name))

        # â¡ promote the current overall best into 'small'
        neg_s, nm = heapq.heappop(self.large)
        heapq.heappush(self.small, (-neg_s, self._inv_pad(nm), nm))

        # â¢ keep |small| == k  (demote its worst if it grew too big)
        if len(self.small) > self.k:
            s, _, nm2 = heapq.heappop(self.small)
            heapq.heappush(self.large, (-s, nm2))

    def get(self):
        # we are now asking for the (k+1)-th best
        self.k += 1

        # promote exactly one more from 'large' into 'small'
        neg_s, nm = heapq.heappop(self.large)
        heapq.heappush(self.small, (-neg_s, self._inv_pad(nm), nm))

        # the root of 'small' is the k-th best overall
        return self.small[0][2]
