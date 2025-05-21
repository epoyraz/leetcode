class MagicDictionary(object):
    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary):
        self.words = set(dictionary)

    def search(self, searchWord):
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            diff = 0
            for a, b in zip(word, searchWord):
                if a != b:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False
