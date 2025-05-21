import heapq

class BIT:
    def __init__(self, n):
        # 1-indexed BIT internally, size = n
        self.n = n
        self.tree = [0] * (n + 1)

    def build(self, data):
        # data: list of length n (0-indexed)
        for i, v in enumerate(data, start=1):
            self.tree[i] += v
        for i in range(1, self.n + 1):
            j = i + (i & -i)
            if j <= self.n:
                self.tree[j] += self.tree[i]

    def update(self, idx, delta):
        # add delta at data[idx] (0-indexed)
        i = idx + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, idx):
        # prefix sum data[0..idx], 0-indexed
        i = idx + 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def find_kth(self, k):
        # find smallest idx such that prefix sum >= k
        # assume 1 <= k <= total sum
        idx = 0
        bit_mask = 1 << (self.n.bit_length())  # largest power of two >= n
        while bit_mask:
            t = idx + bit_mask
            if t <= self.n and self.tree[t] < k:
                idx = t
                k -= self.tree[t]
            bit_mask >>= 1
        return idx  # idx is 1-based sum < k, so 0-based index is idx

class Solution:
    def busiestServers(self, k, arrival, load):
        # BIT to track which servers are free (1 = free, 0 = busy)
        bit = BIT(k)
        bit.build([1] * k)

        busy = []   # min-heap of (free_time, server_id)
        count = [0] * k
        m = len(arrival)

        for i in range(m):
            t = arrival[i]
            # free up servers that have completed by time t
            while busy and busy[0][0] <= t:
                _, srv = heapq.heappop(busy)
                bit.update(srv, +1)  # mark server free

            # total free?
            total_free = bit.query(k - 1)
            if total_free == 0:
                continue  # drop request

            # preferred server
            start = i % k
            # free in [start..k-1] ?
            free_after = total_free - (bit.query(start - 1) if start > 0 else 0)
            if free_after > 0:
                # the first free in [start..]
                # we want the (prefix before start)+1 -th free in whole
                prev_count = bit.query(start - 1) if start > 0 else 0
                srv = bit.find_kth(prev_count + 1)
            else:
                # wrap around: take the very first free
                srv = bit.find_kth(1)

            # assign request to srv
            count[srv] += 1
            bit.update(srv, -1)  # mark busy
            heapq.heappush(busy, (t + load[i], srv))

        # find max handled
        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
