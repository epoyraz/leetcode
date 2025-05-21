import heapq

class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        MOD = 10**9 + 7
        buy_heap = []   # Max-heap for buy orders: (-price, amount)
        sell_heap = []  # Min-heap for sell orders: (price, amount)

        for price, amount, order_type in orders:
            if order_type == 0:  # Buy order
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_heap)
                    matched = min(amount, sell_amount)
                    amount -= matched
                    sell_amount -= matched
                    if sell_amount > 0:
                        heapq.heappush(sell_heap, (sell_price, sell_amount))
                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))

            else:  # Sell order
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_heap)
                    matched = min(amount, buy_amount)
                    amount -= matched
                    buy_amount -= matched
                    if buy_amount > 0:
                        heapq.heappush(buy_heap, (buy_price, buy_amount))
                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))

        # Sum up remaining amounts in both heaps
        total = sum(amount for _, amount in buy_heap + sell_heap)
        return total % MOD
