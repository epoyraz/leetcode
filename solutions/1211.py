from itertools import combinations

class CombinationIterator:
    def __init__(self, characters, combinationLength):
        self.combos = list(combinations(characters, combinationLength))
        self.index = 0

    def next(self):
        res = ''.join(self.combos[self.index])
        self.index += 1
        return res

    def hasNext(self):
        return self.index < len(self.combos)
