class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]  # product prefix, starting with 1 as identity
        self.zero_index = -1  # last index where a zero was inserted

    def add(self, num):
        if num == 0:
            self.prefix = [1]  # reset after zero
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        if k >= len(self.prefix):
            return 0  # there's a zero within the last k numbers
        return self.prefix[-1] // self.prefix[-k - 1]
