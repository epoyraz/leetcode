import heapq

class StockPrice(object):

    def __init__(self):
        self.timestamp_to_price = {}
        self.max_heap = []
        self.min_heap = []
        self.latest_timestamp = 0

    def update(self, timestamp, price):
        self.timestamp_to_price[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        # Push new entries to both heaps
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        return self.timestamp_to_price[self.latest_timestamp]

    def maximum(self):
        while True:
            price, timestamp = self.max_heap[0]
            if self.timestamp_to_price[timestamp] == -price:
                return -price
            heapq.heappop(self.max_heap)

    def minimum(self):
        while True:
            price, timestamp = self.min_heap[0]
            if self.timestamp_to_price[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
