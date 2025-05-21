from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:
    def __init__(self, n, entries):
        self.available = defaultdict(SortedList)  # movie -> SortedList of (price, shop)
        self.prices = {}  # (shop, movie) -> price
        self.rented = SortedList()  # SortedList of (price, shop, movie)

        for shop, movie, price in entries:
            self.available[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie):
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop, movie):
        price = self.prices[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self):
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
