class OrderedStream:
    def __init__(self, n):
        # 1-indexed storage for values; positions start empty
        self.stream = [''] * (n + 2)
        # ptr is the next ID we're waiting to output
        self.ptr = 1

    def insert(self, idKey, value):
        # Store the incoming value
        self.stream[idKey] = value
        # If this fills the next-expected slot, collect all consecutive
        res = []
        while self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res
