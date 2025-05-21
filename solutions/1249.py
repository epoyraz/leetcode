import bisect

class SnapshotArray(object):
    def __init__(self, length):
        self.data = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        if self.data[index] and self.data[index][-1][0] == self.snap_id:
            self.data[index][-1] = (self.snap_id, val)  # overwrite last if same snap_id
        else:
            self.data[index].append((self.snap_id, val))

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        arr = self.data[index]
        i = bisect.bisect_right(arr, (snap_id, float('inf'))) - 1
        return arr[i][1] if i >= 0 else 0
