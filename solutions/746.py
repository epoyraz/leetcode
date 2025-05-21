class WordFilter(object):

    def __init__(self, words):
        self.lookup = {}
        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                for j in range(length + 1):
                    key = (word[:i], word[j:])
                    self.lookup[key] = index

    def f(self, pref, suff):
        return self.lookup.get((pref, suff), -1)
