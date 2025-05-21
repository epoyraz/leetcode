from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> list of (timestamp, value)

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        items = self.store.get(key, [])
        i = bisect.bisect_right(items, (timestamp, chr(127)))  # find the first > timestamp
        if i == 0:
            return ""
        return items[i - 1][1]
