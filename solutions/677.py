class MapSum(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        total = 0
        for k in self.map:
            if k.startswith(prefix):
                total += self.map[k]
        return total
