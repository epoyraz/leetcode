class Allocator:
    def __init__(self, n):
        self.mem = [0] * n
        self.n = n

    def allocate(self, size, mID):
        i = 0
        while i < self.n:
            if self.mem[i] != 0:
                i += 1
                continue
            j = i
            while j < self.n and self.mem[j] == 0 and j - i + 1 <= size:
                j += 1
            if j - i >= size:
                for k in range(i, i + size):
                    self.mem[k] = mID
                return i
            i = j
        return -1

    def freeMemory(self, mID):
        count = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                self.mem[i] = 0
                count += 1
        return count
