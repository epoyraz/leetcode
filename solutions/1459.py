class Cashier(object):
    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.count = 0
        self.price_map = {pid: price for pid, price in zip(products, prices)}

    def getBill(self, product, amount):
        self.count += 1
        total = sum(self.price_map[pid] * qty for pid, qty in zip(product, amount))
        if self.count % self.n == 0:
            total *= (100 - self.discount) / 100.0
        return total
