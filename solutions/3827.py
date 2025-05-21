import collections
import bisect

class Router(object):
    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.limit = memoryLimit
        # FIFO queue of (source, dest, timestamp)
        self.queue = collections.deque()
        # Set of packets currently stored, for duplicate detection
        self.packet_set = set()
        # Per-destination record: dest -> {'times': [...], 'head': int}
        # 'times' is list of timestamps (in increasing order as added)
        # 'head' is the index of the first active (not yet removed) timestamp
        self.dest_map = {}

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        packet = (source, destination, timestamp)
        # Duplicate?
        if packet in self.packet_set:
            return False

        # Enqueue the new packet
        self.queue.append(packet)
        self.packet_set.add(packet)

        # Record timestamp in dest_map
        rec = self.dest_map.setdefault(destination, {'times': [], 'head': 0})
        rec['times'].append(timestamp)

        # Enforce memory limit: if exceeded, drop oldest
        if len(self.queue) > self.limit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.packet_set.remove((old_source, old_dest, old_time))
            # Advance head in that dest's record
            old_rec = self.dest_map[old_dest]
            old_rec['head'] += 1

        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.packet_set.remove((source, destination, timestamp))
        # Advance head for this destination
        rec = self.dest_map[destination]
        rec['head'] += 1
        return [source, destination, timestamp]

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        rec = self.dest_map.get(destination)
        if not rec:
            return 0
        arr = rec['times']
        h = rec['head']
        # Find leftmost â¥ startTime, rightmost â¤ endTime
        left = bisect.bisect_left(arr, startTime, lo=h)
        right = bisect.bisect_right(arr, endTime, lo=h)
        return right - left
