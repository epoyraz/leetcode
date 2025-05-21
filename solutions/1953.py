import math
import bisect
from collections import deque

class SortedListWithSum:
    def __init__(self):
        self.size = 0
        self.buckets = []
        self.bucket_sums = []

    def _build(self, a=None):
        if a is None:
            a = list(self)
        a.sort()
        self.size = len(a)
        if self.size == 0:
            self.buckets = []
            self.bucket_sums = []
            return
        b = int(math.ceil(math.sqrt(self.size)))
        self.buckets = [a[i:i+b] for i in range(0, self.size, b)]
        self.bucket_sums = [sum(bucket) for bucket in self.buckets]

    def _find_bucket(self, x):
        for i, bucket in enumerate(self.buckets):
            if x <= bucket[-1]:
                return i, bucket
        return len(self.buckets) - 1, self.buckets[-1]

    def add(self, x):
        if self.size == 0:
            self.buckets = [[x]]
            self.bucket_sums = [x]
            self.size = 1
            return
        i, bucket = self._find_bucket(x)
        pos = bisect.bisect_left(bucket, x)
        bucket.insert(pos, x)
        self.bucket_sums[i] += x
        self.size += 1
        if len(bucket) > len(self.buckets) * 50:
            self._build()

    def discard(self, x):
        if self.size == 0:
            return False
        i, bucket = self._find_bucket(x)
        pos = bisect.bisect_left(bucket, x)
        if pos < len(bucket) and bucket[pos] == x:
            bucket.pop(pos)
            self.bucket_sums[i] -= x
            self.size -= 1
            if not bucket:
                self._build()
            return True
        return False

    def __iter__(self):
        for bucket in self.buckets:
            for x in bucket:
                yield x

    def prefix_sum(self, k):
        res = 0
        cnt = k
        for bucket, s in zip(self.buckets, self.bucket_sums):
            if cnt <= 0:
                break
            if len(bucket) <= cnt:
                res += s
                cnt -= len(bucket)
            else:
                for i in range(cnt):
                    res += bucket[i]
                break
        return res

class MKAverage(object):
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.queue = deque()
        self.sl = SortedListWithSum()
        self.total = 0

    def addElement(self, num):
        self.queue.append(num)
        self.sl.add(num)
        self.total += num
        if len(self.queue) > self.m:
            old = self.queue.popleft()
            self.sl.discard(old)
            self.total -= old

    def calculateMKAverage(self):
        if len(self.queue) < self.m:
            return -1
        sum_small = self.sl.prefix_sum(self.k)
        sum_mid = self.sl.prefix_sum(self.m - self.k) - sum_small
        cnt = self.m - 2*self.k
        return sum_mid // cnt
